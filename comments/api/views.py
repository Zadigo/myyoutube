from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from comments.api import serializers
from comments.models import Comment
from notifications.models import Notification
from videos.models import Video


@api_view(['get'])
def list_comments(request, video_id, **kwargs):
    """Return all the comments from the current video"""
    video = get_object_or_404(Video, video_id=video_id)
    comments = video.comment_set.all()
    serializer = serializers.CommentSerializer(
        instance=comments,
        many=True
    )
    return Response(serializer.data)


@api_view(['post'])
@permission_classes([IsAdminUser, IsAuthenticated])
def create_comment(request, video_id, **kwargs):
    """Creates a new comment on the current video"""
    serializer = serializers.ValidateCommentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    video = get_object_or_404(Video, video_id=video_id)
    comment = serializer.save(request, video)

    # notification = Notification.objects.create()

    serializer = serializers.CommentSerializer(instance=comment)
    return Response(serializer.data)


@api_view(['post'])
@permission_classes([IsAdminUser, IsAuthenticated])
def create_reply(request, comment_id, **kwargs):
    """Creates a new reply to a comment"""
    serializer = serializers.ValidateReplySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    reply = serializer.save()

    comment = get_object_or_404(Comment, comment_id=comment_id)
    comment.reply_set.create(
        user=request.user,
        content=None
    )

    serializer = serializers.ReplySerializer(instance=reply)
    return Response(serializer.data)
