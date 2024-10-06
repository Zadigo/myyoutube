from rest_framework import fields
from rest_framework.serializers import Serializer

from playlists.models import Playlist
from playlists.validators import validate_description
from videos.api.serializers import VideoSerializer
from videos.choices import VisibilityChoices
from django.shortcuts import get_object_or_404

from videos.models import Video


class PlaylistSerializer(Serializer):
    id = fields.IntegerField()
    name = fields.CharField()
    videos = VideoSerializer(many=True)
    visibility = fields.ChoiceField(
        VisibilityChoices.choices,
        default=VisibilityChoices.PUBLIC
    )
    created_on = fields.DateTimeField()


class SimplePlaylistSerializer(Serializer):
    id = fields.IntegerField()
    playlist_id = fields.CharField()
    name = fields.CharField()


class ValidateCreatePlaylist(Serializer):
    name = fields.CharField()
    description = fields.CharField(
        allow_null=True,
        validators=[validate_description]
    )
    is_intelligent = fields.BooleanField(default=False)

    def save(self, request, **kwargs):
        setattr(self, '_request', request)
        return super().save(**kwargs)

    def create(self, validated_data):
        playlist, state = Playlist.objects.get_or_create(
            defaults={
                # 'description': validated_data['description'],
                'is_intelligent': validated_data['is_intelligent']
            },
            name=validated_data['name'],
            user=self._request.user
        )
        return playlist


class ValidateAddToPlaylist(Serializer):
    video_id = fields.CharField()
    
    def update(self, instance, validated_data):
        video = get_object_or_404(Video, video_id=validated_data['video_id'])
        instance.videos.add(video)
        return instance
