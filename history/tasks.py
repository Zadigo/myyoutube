from celery import shared_task
from django.db import transaction


@shared_task
def add_video_to_history(user, video):
    try:
        with transaction.atomic():
            item = video.history_set.create(
                user=user
            )
    except Exception as e:
        return e.args
    return item
