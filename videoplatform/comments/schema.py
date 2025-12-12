from comments.models import Comment, Reply
from graphene_django import DjangoObjectType
import graphene
from graphene_django.filter import DjangoFilterConnectionField


class CommentType(DjangoObjectType):
    """GraphQL type for Comment model"""

    number_of_replies = graphene.Int(
        description='Number of replies for the comment')

    class Meta:
        model = Comment
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'id': ['exact'],
            'user__username': ['exact', 'icontains'],
            'content': ['icontains'],
            'from_creator': ['exact'],
            'pinned': ['exact'],
            'created_on': ['exact', 'lt', 'gt'],
        }

    def resolve_number_of_replies(self, info):
        return self.number_of_replies


class ReplyType(DjangoObjectType):
    """GraphQL type for Reply model"""

    class Meta:
        model = Reply
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'id': ['exact'],
            'from_creator': ['exact'],
            'pinned': ['exact'],
            'created_on': ['exact', 'lt', 'gt'],
        }


class CommentsQuery(graphene.ObjectType):
    """GraphQL queries for comments and replies"""

    videocomments = DjangoFilterConnectionField(
        CommentType,
        video_id=graphene.ID(required=True, description='ID of the video')
    )
    commentreplies = DjangoFilterConnectionField(
        ReplyType,
        comment_id=graphene.ID(required=True, description='ID of the comment')
    )

    def resolve_videocomments(self, info, video_id=None, **kwargs):
        """Returns the comments for the given video"""
        if video_id is not None:
            return Comment.objects.filter(video__id=video_id)
        return Comment.objects.none()

    def resolve_commentreplies(self, info, comment_id=None, **kwargs):
        """Returns the replies for the given comment"""
        if comment_id is not None:
            return Reply.objects.filter(comment__id=comment_id)
        return Reply.objects.none()
