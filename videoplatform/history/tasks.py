from celery import shared_task
from django.contrib.auth import get_user_model
from videos.models import Video


@shared_task
def add_video_to_history(user_id: str, video_id: str):
    """Adds the video that is currently watched by the
    user in his history"""
    try:
        video = Video.objects.get(id=video_id)
    except:
        return
    else:
        user = get_user_model().objects.get(id=user_id)
        video.history_set.create(user=user)
        return user.id
