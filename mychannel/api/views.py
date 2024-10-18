from rest_framework.generics import (GenericAPIView, ListAPIView,
                                     RetrieveAPIView)
from rest_framework.mixins import Response
from rest_framework.permissions import AllowAny

from comments.api.serializers import ReplySerializer
from mychannel import models
from mychannel.api.serializers import UserChannelSerializer
from mychannel.serializers import SearchSerializer
from videos.api.serializers import VideoSerializer


class UserChannelAPI(RetrieveAPIView):
    serializer_class = UserChannelSerializer
    queryset = models.UserChannel.objects.all()
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'channel_id'
    lookup_field = 'reference'


class UserChannelsAPI(ListAPIView):
    serializer_class = UserChannelSerializer
    queryset = models.UserChannel.objects.all()
    permission_classes = [AllowAny]


class SearchUserChannelAPI(GenericAPIView):
    serializer_class = SearchSerializer
    queryset = models.UserChannel.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'reference'
    lookup_url_kwarg = 'channel_id'

    def post(self, request, *args, **kwargs):
        search_serializer = self.get_serializer(data=request.data)
        search_serializer.is_valid(raise_exception=True)

        channel = self.get_object()
        queryset = channel.video_set.active_videos()

        video_name = search_serializer.validated_data.get('video_name')
        if video_name is not None:
            queryset = queryset.filter(title__iexact=video_name)

        tags = search_serializer.validated_data.get('tags', [])
        if tags:
            queryset = queryset.filter(tags__name__in=tags)

        serializer = VideoSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)
