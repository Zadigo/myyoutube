from django.db.models import QuerySet
from django.db.models.expressions import Case, When
from django.db.models.fields import BooleanField


class PlaylistManager(QuerySet):
    def annotated_playlist(self, user, current_video):
        """
        The playlist queryset annotated with whether the
        current video is the user's playlist or not
        """
        playlists = self.filter(user=user)

        user_playlist_for_this_video = list(
            current_video.playlist_set.filter(
                user=user).values_list('name', flat=True)
        )
        logic = When(name__in=user_playlist_for_this_video, then=True)
        cases = Case(logic, default=False, output_field=BooleanField())
        annotated_playlists = playlists.annotate(video_in_playlist=cases)
        return annotated_playlists
