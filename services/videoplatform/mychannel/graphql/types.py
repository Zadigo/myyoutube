from graphene_django import DjangoObjectType
from mychannel.models import UserChannel, ChannelPlaylist, ChannelTag
from django.db.models import QuerySet
from mychannel.models import UserChannel, ChannelPlaylist, ChannelTag

class UserChannelType(DjangoObjectType):
    class Meta:
        model = UserChannel
        fields = '__all__'

    @classmethod
    def get_queryset(cls, queryset: QuerySet[UserChannel], info):
        return queryset.select_related('user').prefetch_related('tags').all()


class ChannelPlaylistType(DjangoObjectType):
    class Meta:
        model = ChannelPlaylist
        fields = '__all__'


class ChannelTagsType(DjangoObjectType):
    class Meta:
        model = ChannelTag
        fields = '__all__'
