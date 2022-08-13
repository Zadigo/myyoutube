from django.contrib import messages
from django.db.transaction import atomic
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.generic import DetailView
from videos.choices import VisibilityChoices
from videos.models import Playlist, Video


class PlaylistView(DetailView):
    model = Playlist
    template_name = 'pages/playlist.html'
    context_object_name = 'playlist'
    
    def get_queryset(self):
        return super().get_queryset()


@require_POST
@atomic
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
@atomic
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
