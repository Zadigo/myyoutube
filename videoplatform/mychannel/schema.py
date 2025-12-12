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


class MyChannelQuery(graphene.ObjectType):
    user_channel = graphene.Field(UserChannelType, reference=graphene.String(required=True))
    channel_playlists = graphene.List(ChannelPlaylistType, channel_reference=graphene.String(required=True))
    channel_tags = graphene.List(ChannelTagsType)

    def resolve_user_channel(self, info, reference):
        try:
            return UserChannel.objects.get(reference=reference)
        except UserChannel.DoesNotExist:
            return None 

    def resolve_channel_playlists(self, info, channel_reference):
        channel = UserChannel.objects.get(reference=channel_reference)
        return ChannelPlaylist.objects.filter(user_channel=channel)

    def resolve_channel_tags(self, info):
        return ChannelTag.objects.all()
