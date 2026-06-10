from celery import shared_task
from django.contrib.auth import get_user_model
from videos.models import Video
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def add_video_to_history(user_id: str, video_id: str):
    """Adds the video that is currently watched by the
    user in his history"""
    try:
        video = Video.objects.get(id=video_id)
    except Video.DoesNotExist:
        logger.error(f"Video with id {video_id} does not exist.")
        return
    else:
        user = get_user_model().objects.get(id=user_id)
        video.history_set.create(user=user)
        logger.info(f"Added video with id {video_id} to history for user with id {user_id}.")
        return user.id
