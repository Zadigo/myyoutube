from celery import shared_task
from celery.utils.log import get_logger
from django.contrib.auth import get_user_model
from notifications.models import Notification

logger = get_logger('notifications')


@shared_task
def add_notification(user_id: int, validated_data: dict):
    try:
        user = get_user_model().objects.get(id=user_id)
    except get_user_model().DoesNotExist:
        logger.error(f'User with id {user_id} does not exist.')
        return
    Notification.objects.create(user=user, **validated_data)
    return {'status': 'Notification added', 'user_id': user_id, 'video': validated_data.get('video')}


@shared_task
def toggle_read_notification(notification_id: str | int):
    try:
        notification = Notification.objects.get(id=notification_id)
    except Notification.DoesNotExist:
        logger.error(f'Notification with id {notification_id} does not exist.')
        return {'status': 'Notification not found', 'notification_id': notification_id}
    else:
        notification.read = not notification.read
        notification.save()
        return {'status': 'Notification read status toggled', 'notification_id': notification_id, 'read': notification.read}
