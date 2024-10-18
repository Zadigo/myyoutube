from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, GenericAPIView

from comments.api import serializers
from comments.models import Comment, Reply
from notifications.models import Notification
from videos.models import Video


class CommentAPI(GenericAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = []
    lookup_field = 'reference'
    lookup_url_kwarg = 'video_id'

    def get(self, request, video_id, *args, **kwargs):
        sort_descending = request.GET.get('desc', 'true')
        video = get_object_or_404(Video, video_id=video_id)

        fields = ['-id', '-created_on']
        if sort_descending != 'true':
            fields = ['id', 'created_on']

        comments = video.comment_set.order_by(*fields)
        serializer = self.get_serializer(instance=comments, many=True)
        return Response(serializer.data)


class CreateReplyAPI(CreateAPIView):
    serializer_class = serializers.ReplySerializer
    queryset = Comment.objects.all()
    permission_classes = []

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['comment'] = self.get_object()
        return context
