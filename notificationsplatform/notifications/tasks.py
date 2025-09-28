from celery import shared_task
from celery.utils.log import get_logger
from django.contrib.auth import get_user_model

logger = get_logger('notifications')


@shared_task
def add_notification(user_id: str | int, video_id: str | int, notification_type: str):
    pass


@shared_task
def toggle_read_notification(notification_id: str | int):
    pass
