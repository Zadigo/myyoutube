import graphene
from community_notes.api.serializers import CreateNoteSerializer
from community_notes.models import CommunityNote, CommunityNoteSource
from community_notes.tasks import apply_vote
from django.contrib.auth import get_user_model
from django.db.models import Q
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
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        author = graphene.String(
            required=True, description="Username or YouTube ID of the author")
        subject_creator_id = graphene.String(required=True)

    def mutate(root, info, title, description, author, subject_creator_id):
        try:
            author = USER_MODEL.objects.get(
                Q(username=author) |
                Q(youtube_id=author)
            )
        except USER_MODEL.DoesNotExist:
            raise Exception('Author not found')
        else:
            instance = CommunityNote.objects.create(
                title=title,
                description=description,
                author=author,
                subject_creator_id=subject_creator_id
            )

            return CommunityNoteMutation(reference=instance.reference)



class CommunityNoteVoteMutation(graphene.Mutation):
    reference = graphene.String()

    class Arguments:
        reference = graphene.String(
            required=True
        )
        vote_type = graphene.String(
            required=True, 
            description="'upvote' or 'downvote'"
        )
        reason = graphene.String(
            required=False, 
            description="Optional reason for downvote"
        )

    def mutate(root, info, reference, vote_type, reason=None):
        try:
            note = CommunityNote.objects.get(reference=reference)
        except CommunityNote.DoesNotExist:
            raise Exception('Community Note not found')
        else:
            apply_vote.apply_async(
                args=[
                    note.id, 
                    1 if vote_type == 'upvote' else -1, 
                    info.context.user.id,
                    reason
                ]
            )
            return CommunityNoteVoteMutation(reference=note.reference)
