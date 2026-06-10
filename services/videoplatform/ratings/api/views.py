from ratings.api import serializers
from ratings.models import Rating
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from videos.models import Video
from django.shortcuts import get_object_or_404
from django.core.cache import cache


# TODO: Simplify to a generic api view
class RateVideo(CreateAPIView, UpdateAPIView):
    """Endpoint used to like or dislike a video. It also
    can modidify the subscription mode to the video for 
    the current given user"""

    serializer_class = serializers.BaseValidateRating
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'video__video_id'
    lookup_url_kwarg = 'video_id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        rating = self.get_object()
        if rating is not None:
            video = rating.video
        else:
            params = {'video_id': self.kwargs[self.lookup_url_kwarg]}
            video = get_object_or_404(Video, **params)
        context['video_instance'] = video
        return context

    def get_queryset(self):
        qs = self.filter_queryset(self.queryset)
        params = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}
        return qs.filter(**params)

    def get_object(self) -> Rating | None:
        qs = self.get_queryset()
        if qs.exists():
            try:
                params = {'user': self.request.user}
                return qs.get(**params)
            except:
                pass
        # By returning None we are forcing
        # the serializer in creation mode
        # since there is no instance
        return None

    def base_response(self):
        rating = self.get_object()
        serializer = serializers.RatingSeralizer(instance=rating)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return self.base_response()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return self.base_response()
