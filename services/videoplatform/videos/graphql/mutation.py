from typing import Any

import graphene
from graphene import relay
from graphql import GraphQLResolveInfo
from videos.models import Video, Tag
from videos.graphql.types import VideosType
from videos.graphql.utils import CategoryEnum, CommentingStrategyEnum, VisibilityEnum


class CreateVideoMutation(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        description = graphene.String()
        age_restricted = graphene.Boolean()
        category = CategoryEnum()
        visibility = VisibilityEnum()
        recording_date = graphene.Date()
        recording_language = graphene.String()
        tags = graphene.List(graphene.String)
        channelPlaylistId = graphene.String()
        comment_strategy = CommentingStrategyEnum()

    video = graphene.Field(VideosType)

    @classmethod
    def mutate(cls, root, info: GraphQLResolveInfo, input: dict[str, Any]):
        if not info.context.user.is_authenticated:
            raise Exception("Authentication required")

        input['user'] = info.context.user
        input['user_channel'] = info.context.user.userchannel_set.get()
        instance = Video.objects.create(**input)

        channel_playlist_id = input.pop('channelPlaylistId', None)
        if channel_playlist_id is not None:
            channel_playlist = instance.user_channel.channelplaylist_set.filter(
                id=channel_playlist_id
            ).first()

            if channel_playlist:
                instance.channel_playlist = channel_playlist
                instance.save()

        tags = input.pop('tags', [])
        if tags:
            objs = []
            for name in tags:
                tag, _ = Tag.objects.get_or_create(name=name)
                objs.append(tag)
            instance.tags.add(*objs)

        return CreateVideoMutation(video=instance)
