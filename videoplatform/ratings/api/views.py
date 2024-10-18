from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ratings.api import serializers
from videos.models import Video


@api_view(http_method_names=['post'])
@permission_classes([IsAuthenticated])
def rate_video(request, video_id, **kwargs):
    video = get_object_or_404(Video, video_id=video_id)

    if not video.active or video.visibility == 'Private':
        return Response({}, status=404)

    rating_queryset = video.rating_set.filter(user=request.user)
    if rating_queryset.exists():
        try:
            rating = rating_queryset.get()
        except:
            return Response({}, status=404)
        else:
            serializer = serializers.ValidateSubscription(
                instance=rating,
                data=request.data
            )
    else:
        serializer = serializers.ValidateRating(
            data=request.data
        )
    serializer.is_valid(raise_exception=True)
    serializer.save(request, video)
    return Response({})
