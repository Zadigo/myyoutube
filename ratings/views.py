from django.contrib import messages
from django.db import transaction
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from videos.models import Video

from ratings.models import Rating


def _retrieve_video(request):
    reference = request.POST.get('video')
    return get_object_or_404(Video, reference=reference)


def _create_notification(request, video):
    return video.notification_set.create(
        user=request.user,
        notification_type='Like'
    )


def _delete_notification(request, video, is_switch=False):
    notification = video.notification_set.filter(
        user=request.user,
        video=video,
        notification_type='Like'
    )
    if notification.exists():
        notification.delete()
    return True


@require_POST
@transaction.atomic
def like_video(request, **kwargs):
    video = _retrieve_video(request)
    result, likes_count = Rating.objects.add_like(
        request, video, 'video'
    )
    if not result:
        messages.error(request, "An error occured - LIK-AD", extra_tags='alert-danger')
    _create_notification(request, video)
    return JsonResponse(data={'state': result, 'count': likes_count})


@require_POST
@transaction.atomic
def dislike_video(request, **kwargs):
    video = _retrieve_video(request)
    result, likes_count = Rating.objects.add_dislike(
        request, video, 'video'
    )
    if not result:
        messages.error(request, "An error occured - DIS-AD", extra_tags='alert-danger')
    return JsonResponse(data={'state': result, 'count': likes_count})


@require_POST
@transaction.atomic
def remove_like(request, **kwargs):
    video = _retrieve_video(request)
    result, likes_count = Rating.objects.remove_like_or_dislike(
        request, video, 'video'
    )
    if not result:
        messages.error(request, "An error occured - DIS-AD", extra_tags='alert-danger')
    _delete_notification(request, video)
    return JsonResponse(data={'state': result, 'count': likes_count})


@require_POST
@transaction.atomic
def switch_state(request):
    video = _retrieve_video(request)
    # Since there are buttons with multiple states,
    # there are situations where a video might be
    # rated and the user clicks directly one of the
    # other ratings which will require switching from
    # like to dislike and inversely
    result, likes_count = Rating.objects.switch_rating(request, video)
    if not result:
        messages.error(request, "An error occured - DIS-AD", extra_tags='alert-danger')

    # if '' == 'like':
    #     _create_notification(request, video)
    # if '' == 'dislike':
    #     _delete_notification(request, video)
    return JsonResponse(data={'state': result, 'count': likes_count})


@require_POST
@transaction.atomic
def rate_comment(request, **kwargs):
    pass


@require_POST
@transaction.atomic
def rate_reply(request, **kwargs):
    pass
