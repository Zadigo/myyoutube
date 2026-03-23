import graphene
from graphene import relay
from videos.models import Video, Tag
from videos.graphql.types import VideosType


class CreateVideoMutation(relay.ClientIDMutation):
    class Input:
        title = graphene.String(required=True)
        description = graphene.String()
        video_id = graphene.String(required=True)
        age_restricted = graphene.Boolean()
        category = graphene.String()
        visibility = graphene.String()
        recording_date = graphene.Date()
        recording_language = graphene.String()
        tags = graphene.List(graphene.String)

    video = graphene.Field(VideosType)

    # @classmethod
    # def mutate_and_get_payload(cls, root, info, **input):
    #     user = info.context.user
    #     if not user.is_authenticated:
    #         raise Exception("Authentication required")

    #     video = Video.objects.create(
    #         title=input['title'],
    #         description=input.get('description', ''),
    #         video_id=input['video_id'],
    #         age_restricted=input.get('age_restricted', False),
    #         category=input.get('category', ''),
    #         visibility=input.get('visibility', 'Private'),
    #         recording_date=input.get('recording_date'),
    #         recording_language=input.get('recording_language', ''),
    #         user=user
    #     )

    #     tags_input = input.get('tags', [])
    #     for tag_name in tags_input:
    #         tag, created = Tag.objects.get_or_create(name=tag_name)
    #         video.tags.add(tag)

    #     return CreateVideoMutation(video=video)
