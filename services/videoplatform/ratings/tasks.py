from celery import shared_task
from ratings.models import Rating
from django.contrib.auth import get_user_model
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def create_rating(video_id: str, user_id: int, rating: int):
    user = get_user_model().objects.get(id=user_id)
    instance = Rating.objects.get(video_id=video_id, user=user)
    instance.rating = rating
    instance.save()
    logger.info(f'Rating updated for video {video_id} by user {user_id}')


@shared_task
def notify_user(user_id: str):
    user = get_user_model().objects.get(id=user_id)
    # Add your notification logic here
    logger.info(f'Notification sent to user {user_id}')
