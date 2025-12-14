from weakref import ref
import graphene
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from factchecking.models import FactCheck
from reportsources.models import ReportSource


class FactCheckType(DjangoObjectType):
    class Meta:
        model = FactCheck
        fields = '__all__'


class FactCheckQuery(graphene.ObjectType):
    factcheck = graphene.Field(FactCheckType, id=graphene.Int(required=True))
    allfactchecks = graphene.List(FactCheckType)
    factcheck_by_reference = graphene.Field(
        FactCheckType,
        reference=graphene.String(required=True)
    )

    def resolve_factcheck(self, info, id):
        try:
            return FactCheck.objects.get(id=id)
        except FactCheck.DoesNotExist:
            return None

    def resolve_allfactchecks(self, info, **kwargs):
        return FactCheck.objects.all()

    def resolve_factcheck_by_reference(self, info, reference):
        try:
            return FactCheck.objects.get(reference=reference)
        except FactCheck.DoesNotExist:
            return None


class FactCheckMutation(graphene.Mutation):
    factcheck = graphene.Field(FactCheckType)

    class Arguments:
        reference = graphene.String(required=False)
        start_time = graphene.Time(required=True)
        end_time = graphene.Time(required=True)
        author = graphene.String(required=True)
        video_id = graphene.String(required=True)
        sources = graphene.List(graphene.String, required=True)
        explanation = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, start_time, end_time, author, video_id, sources, explanation, reference=None):
        print(info.context.user)
        if reference is not None:
            try:
                factcheck = FactCheck.objects.get(reference=reference)
            except FactCheck.DoesNotExist:
                return None
            else:
                # factcheck.active = active
                # factcheck.save()
                return FactCheckMutation(factcheck=factcheck)
        else:
            factcheck = FactCheck(
                start_time=start_time,
                end_time=end_time,
                author_id=author,
                video_id=video_id,
                explanation=explanation
            )
            factcheck.save()

            instances = []
            for source in sources:
                instance, _ = ReportSource.objects.get_or_create(url=source)
                instances.append(instance)

            factcheck.factcheck_sources.set(instances)
            factcheck.save()
        return FactCheckMutation(factcheck=factcheck)
