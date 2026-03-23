import graphene
from graphql import GraphQLResolveInfo
from mychannel.models import UserChannel
from mychannel.graphql.types import UserChannelType, ChannelPlaylistType, ChannelTagsType
from django.core.cache import cache

class MyChannelQuery(graphene.ObjectType):
    all_user_channels = graphene.List(
        UserChannelType
    )
    user_channel = graphene.Field(
        UserChannelType, 
        reference=graphene.String(required=True)
    )
    channel_playlists = graphene.List(
        ChannelPlaylistType, 
        channel_reference=graphene.String(required=True)
    )
    channel_tags = graphene.List(
        ChannelTagsType,
        channel_reference=graphene.String(required=True)
    )

    def resolve_all_user_channels(root, info: GraphQLResolveInfo):
        cache_key = 'all_user_channels'
        channels = cache.get(cache_key)
        if not channels:
            channels = UserChannel.objects.all()
            cache.set(cache_key, channels, timeout=(15 * 60))  # Cache for 15 minutes
        return channels

    def resolve_user_channel(root, info: GraphQLResolveInfo, reference: str):
        try:
            return UserChannel.objects.get(reference=reference)
        except UserChannel.DoesNotExist:
            return None 

    def resolve_channel_playlists(root, info: GraphQLResolveInfo, channel_reference: str):
        cache_key = f'channel_playlists_{channel_reference}'
        playlists = cache.get(cache_key)

        if not playlists:
            channel = UserChannel.objects.get(reference=channel_reference)
            playlists = channel.playlist_set.all()
            cache.set(cache_key, playlists, timeout=(15 * 60))  # Cache for 15 minutes
        return playlists

    def resolve_channel_tags(root, info: GraphQLResolveInfo, channel_reference: str):
        cache_key = f'channel_tags_{channel_reference}'
        tags = cache.get(cache_key)
        if not tags:
            channel = UserChannel.objects.get(reference=channel_reference)
            tags = channel.tags.all()
            cache.set(cache_key, tags, timeout=(15 * 60))  # Cache for 15 minutes
        return tags
