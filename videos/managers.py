from django.db.models import QuerySet
from django.db.models.expressions import When, Case
from django.db.models import F
from django.db.models.fields import BooleanField
from django.utils.functional import cached_property


class VideoManager(QuerySet):
    def user_rating(self, user, video):
        ratings_from_user = video.rating_set.filter(
            user=user,
            video=video
        )
        if ratings_from_user.exists():
            rating = ratings_from_user.get()
            if rating.rating_type == 'Like':
                return 'liked'
            else:
                return 'disliked'
        else:
            return False


class PlaylistManager(QuerySet):
    def annotated_playlist(self, user, current_video):
        """
        The playlist queryset annotated with whether the
        current video is the user's playlist or not

        Args:
            user (type): the current user
            current_video (type): the current video

        Returns:
            queryset: annotated queryset
        """
        playlists = self.filter(user=user)

        user_playlist_for_this_video = list(
            current_video.playlist_set.filter(user=user).values_list('name', flat=True)
        )
        logic = When(name__in=user_playlist_for_this_video, then=True)
        cases = Case(logic, default=False, output_field=BooleanField())
        annotated_playlists = playlists.annotate(video_in_playlist=cases)
        return annotated_playlists
