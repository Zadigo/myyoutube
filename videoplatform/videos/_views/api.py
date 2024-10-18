
import uuid

from django.db.transaction import atomic
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from videos.models import Video


@require_POST
def add_view_count(request, **kwargs):
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
                with atomic():
                    video.mediaview_set.create(
                        user=request.user,
                        duration=duration,
                        ended_at=current_time
                    )
            except Exception:
                pass
            else:
                return_data.update(
                    {'state': True, 'view_id': data.get('uuid')})
    return JsonResponse(data=return_data)
