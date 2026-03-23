import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLResolveInfo
from mychannel.models import UserChannel, ChannelPlaylist, ChannelTag
from mychannel.graphql.types import UserChannelType, ChannelPlaylistType, ChannelTagsType
from django.core.cache import cache

class MyChannelQuery(graphene.ObjectType):
    user_channel = graphene.Field(
        UserChannelType, 
        reference=graphene.String(required=True)
    )
    channel_playlists = graphene.List(
        ChannelPlaylistType, 
        channel_reference=graphene.String(required=True)
    )
    channel_tags = graphene.List(
        ChannelTagsType
    )

    def resolve_user_channel(root, info: GraphQLResolveInfo, reference: str):
        try:
            return UserChannel.objects.get(reference=reference)
        except UserChannel.DoesNotExist:
            return None 

    def resolve_channel_playlists(root, info: GraphQLResolveInfo, channel_reference: str):
        channel = UserChannel.objects.get(reference=channel_reference)
        qs = ChannelPlaylist.objects.filter(user_channel=channel)
        cache_key = f'channel_playlists_{channel_reference}'
        cache.set(cache_key, qs, timeout=(15 * 60))  # Cache for 15 minutes
        return qs

    def resolve_channel_tags(root, info: GraphQLResolveInfo):
        cache_key = 'channel_tags'
        tags = cache.get(cache_key)
        if not tags:
            tags = ChannelTag.objects.all()
            cache.set(cache_key, tags, timeout=(15 * 60))  # Cache for 15 minutes
        return tags
