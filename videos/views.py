import json
import uuid

from django.contrib import messages
from django.core.cache import cache
from django.db import transaction
from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.generic import DetailView, ListView

from videos.choices import VisibilityChoices
from videos.models import Playlist, Video


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
            raise Http404(_(f"No {queryset.model._meta.verbose_name} found matching the query"))
        return video


class FeedMixin(ListView):
    model = Video
    queryset = Video.objects.filter(active=True)
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
        if self.request.user.is_authenticated:
            video = super().get_object()
            
            reverse_accessor = video.rating_set
            context['likes'] = reverse_accessor.filter(rating_type='Like').count()
            context['dislikes'] = reverse_accessor.filter(rating_type='Dislike').count()
            context['user_rating'] = Video.objects.user_rating(
                self.request.user, video
            )

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


class PlaylistView(DetailView):
    model = Playlist
    template_name = 'pages/playlist.html'
    context_object_name = 'playlist'
    
    def get_queryset(self):
        return super().get_queryset()


@require_POST
@transaction.atomic
def new_playlist(request, **kwargs):
    data = {'state': False}
    reference = request.POST.get('reference', None)
    playlist_name = request.POST.get('name', None)

    if (playlist_name is not None and 
            reference is not None):
        visibility = request.POST.get('visibility', VisibilityChoices.PUBLIC)
        visibilities = {
            'Public': VisibilityChoices.PUBLIC,
            'Private': VisibilityChoices.PRIVATE
        }

        try:
            visibility = visibilities[visibility]
        except:
            visibility = VisibilityChoices.PUBLIC
        
        new_playlist = Playlist.objects.create(
            user=request.user,
            name=playlist_name,
            visibility=visibility
        )

        video = get_object_or_404(Video, reference=reference)
        new_playlist.videos.add(video)
    
        data.update({'state': True, 'id': new_playlist.id})
    else:
        messages.error(
            request,
            "An error occured - PLA-DE",
            extra_tags='alert-danger'
        )
    return JsonResponse(data=data)


@require_POST
@transaction.atomic
def add_or_remove_video_in_playlist(request, **kwargs):
    data = {'state': False}
    reference = request.POST.get('reference', None)
    playlist_id = request.POST.get('id', None)

    if playlist_id.isnumeric():
        playlist_id = int(playlist_id)

    if reference is not None and playlist_id is not None:
        video = get_object_or_404(Video, reference=reference)
        playlist_to_add = get_object_or_404(Playlist, id=playlist_id)
        
        playlists = video.playlist_set.filter(
            id=playlist_id
        )
        try:
            playlist = playlists.get()
        except:
            playlist = None

        if playlist is None:
            video.playlist_set.add(playlist_to_add)
        else:
            video.playlist_set.remove(playlist)

        data.update({'state': True})
    else:
        messages.error(
            request,
            "An error occured - PLA-ER",
            extra_tags='alert-danger'
        )
    return JsonResponse(data=data)


def relative_change(end_time, start_time):
    return round(float((end_time - start_time) / start_time), 3)


@require_POST
def count_view(request, **kwargs):
    return_data = {'state': False}
    seeked = request.POST.get('seeked', None)
    duration = request.POST.get('duration', 0)
    current_time = request.POST.get('current_time', 0)

    duration = float(duration)
    current_time = float(current_time)

    # if seeked:
    #     change = relative_change()

    if duration > 0 and seeked is not None and current_time > 0:
        view_data = request.session.get('view_data', None)
        data = view_data or {'uuid': str(uuid.uuid4()), 'videos': []}

        video = get_object_or_404(Video, reference=kwargs.get('reference'))
        references = data['videos']
        # To prevent people from inflating the views
        # more than it should be, register the videos
        # that they have watched within a session and
        # only create a view if its not in these
        if video.reference not in references:
            references.append(video.reference)
            data.update({'videos': references})

            request.session['view_data'] = data

            try:
                with transaction.atomic():
                    video.mediaview_set.create(
                        user=request.user,
                        duration=duration,
                        ended_at=current_time
                    )
            except Exception:
                pass
            else:
                return_data.update({'state': True, 'view_id': data.get('uuid')})
    return JsonResponse(data=return_data)
