from playlists.api.serializers import (PlaylistSerializer,
                                       SimplePlaylistSerializer,
                                       ValidateAddToPlaylist,
                                       ValidateCreatePlaylist)
from playlists.models import Playlist
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   UpdateModelMixin)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ListPlaylists(ListModelMixin, GenericAPIView):
    http_method_names = ['get']
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        is_simple = self.request.GET.get('simple', 0)
        if is_simple == '1':
            self.serializer_class = SimplePlaylistSerializer

        serializer = self.serializer_class(
            instance=queryset,
            many=True
        )
        return Response(serializer.data)

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class CreatePlaylist(CreateModelMixin, GenericAPIView):
    http_method_names = ['post']
    serializer_class = ValidateCreatePlaylist
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        playlist = serializer.save(request)
        playlist_serializer = PlaylistSerializer(instance=playlist)
        return Response(playlist_serializer.data)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise AuthenticationFailed(detail={
                'token': 'User is not authenticated'
            })

        playlists = Playlist.objects.filter(user=self.request.user)
        return playlists


class AddToPlaylist(UpdateModelMixin, GenericAPIView):
    http_method_names = ['post']
    serializer_class = ValidateAddToPlaylist
    lookup_field = 'playlist_id'
    lookup_url_kwarg = 'playlist_id'
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.update(request)

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

        playlist_serializer = PlaylistSerializer(instance=instance)
        return Response(playlist_serializer.data)

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)
