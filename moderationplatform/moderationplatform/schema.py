import graphene
from accounts.schema import AccountsQuery
from community_notes.schema import (CommunityNoteMutation, CommunityNoteQuery,
                                    CommunityNoteVoteMutation)
from graphene_django.debug import DjangoDebug


class ModerationQuery(CommunityNoteQuery, AccountsQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')


class ModerationMutation(graphene.ObjectType):
    create_community_note = CommunityNoteMutation.Field()
    create_community_note_vote = CommunityNoteVoteMutation.Field()


schema = graphene.Schema(query=ModerationQuery, mutation=ModerationMutation)
