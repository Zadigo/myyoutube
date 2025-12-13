import graphene
from community_notes.api.serializers import CreateNoteSerializer
from community_notes.models import CommunityNoteSource, CommunityNote
from django.contrib.auth import get_user_model
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation

USER_MODEL = get_user_model()


class CommunityNoteSourceType(DjangoObjectType):
    class Meta:
        model = CommunityNoteSource
        fields = '__all__'


class CommunityNoteType(DjangoObjectType):
    class Meta:
        model = CommunityNote
        interface = (graphene.relay.Node,)
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains'],
            'author__username': ['exact', 'icontains'],
            'subject_creator_id': ['exact', 'icontains'],
            'is_validated': ['exact'],
            'status': ['exact'],
            'created_on': ['exact', 'lt', 'gt'],
            'score': ['exact', 'lt', 'gt'],
            'upvotes': ['exact', 'lt', 'gt'],
            'downvotes': ['exact', 'lt', 'gt']
        }


class CommunityNoteConnection(graphene.relay.Connection):
    class Meta:
        node = CommunityNoteType


class CommunityNoteQuery(graphene.ObjectType):
    allsources = graphene.List(CommunityNoteSourceType)
    note = graphene.Field(CommunityNoteType, id=graphene.ID(required=True))
    allnotes = relay.ConnectionField(CommunityNoteConnection)

    def resolve_allsources(self, info, **kwargs):
        return CommunityNoteSource.objects.all()

    def resolve_allnotes(self, info, **kwargs):
        return CommunityNote.objects.all()


# class CommunityNoteMutation(SerializerMutation):
#     class Meta:
#         serializer_class = CreateNoteSerializer


class CommunityNoteMutation(graphene.Mutation):
    reference = graphene.String()

    class Arguments:
        author = graphene.String()
        subject_creator_id = graphene.Int()

    def mutate(root, info, author, subject_creator_id):
        author = USER_MODEL.objects.get(id=author)
        
        instance = CommunityNote.objects.create(
            author=author, 
            subject_creator_id=subject_creator_id
        )
        
        return CommunityNoteMutation(reference=instance.reference)
