import graphene
from graphene_django import DjangoObjectType
from mychannel.models import UserChannel, ChannelPlaylist, ChannelTag


class UserChannelType(DjangoObjectType):
    class Meta:
        model = UserChannel
        fields = '__all__'


class ChannelPlaylistType(DjangoObjectType):
    class Meta:
        model = ChannelPlaylist
        fields = '__all__'


class ChannelTagsType(DjangoObjectType):
    class Meta:
        model = ChannelTag
        fields = '__all__'
