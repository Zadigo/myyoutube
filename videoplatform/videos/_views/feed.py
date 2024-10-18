from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView

from playlists.models import Playlist
from videos.models import Video

from ..utils import vue_dict


class BaseDetailView(DetailView):
    model = Video
    queryset = Video.objects.all()
    context_object_name = 'video'
    pk_url_kwarg = 'reference'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        reference = self.kwargs.get(self.pk_url_kwarg)
        if reference is not None:
            queryset = queryset.filter(reference=reference)

        if reference is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "reference in the URLconf." % self.__class__.__name__
            )

        try:
            video = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                _(f"No {queryset.model._meta.verbose_name} found matching the query"))
        return video


class FeedMixin(ListView):
    model = Video
    queryset = Video.objects.all()
    context_object_name = 'videos'


class FeedView(FeedMixin, ListView):
    template_name = 'pages/feed.html'


class SearchView(FeedMixin, ListView):
    template_engine = 'pages/search.html'


class VideoView(BaseDetailView):
    template_name = 'pages/video.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            video = super().get_object()
            video.history_set.create(user=self.request.user)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        video = super().get_object()
        context['vue_video'] = {
            "id": video.id,
            "name": video.title,
            "comments": list(video.comment_set.values('id', 'content', 'user__username', 'pinned'))
        }

        if self.request.user.is_authenticated:
            reverse_accessor = video.rating_set
            context['likes'] = reverse_accessor.filter(
                rating_type='Like').count()
            context['dislikes'] = reverse_accessor.filter(
                rating_type='Dislike').count()
            context['user_rating'] = Video.objects.user_rating(
                self.request.user, video)

            context['is_subscribed'] = False
            subscription = video.user_channel.subscribers.filter(
                username=self.request.user.username
            )
            if subscription.exists():
                context.update({'is_subscribed': True})

            playlists = Playlist.objects.annotated_playlist(
                self.request.user, video
            )
            context['playlists'] = playlists
        return context
