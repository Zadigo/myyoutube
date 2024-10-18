from celery import shared_task
from django.db import transaction


@shared_task
def add_new_view(user, video, duration, ended_at):
    try:
        with transaction.atomic():
            media_view = video.mediaview_set.create(
                user=user,
                duration=duration,
                ended_at=ended_at
            )
    except Exception as e:
        return e.args
    return media_view
