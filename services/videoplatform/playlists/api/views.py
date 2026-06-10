from playlists.api import serializers
from playlists.api.serializers import (PlaylistSerializer,
                                       SimplePlaylistSerializer,
                                       ValidateAddToPlaylist,
                                       ValidateCreatePlaylist)
from playlists.models import Playlist
from rest_framework import status
from rest_framework.generics import (CreateAPIView, GenericAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ListPlaylists(ListAPIView):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class CreatePlaylist(CreateAPIView):
    serializer_class = ValidateCreatePlaylist
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class AddToPlaylist(RetrieveUpdateAPIView):
    """Add a new video to the selected playlist"""

    serializer_class = ValidateAddToPlaylist
    queryset = Playlist.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'playlist_id'
    lookup_url_kwarg = 'playlist_id'

    def retrieve(self, request, *args, **kwargs):
        qs = self.get_queryset()
        serializer = serializers.PlaylistSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return self.retrieve(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)
