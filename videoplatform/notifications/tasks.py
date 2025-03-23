from celery import shared_task
from celery.utils.log import get_logger
from django.contrib.auth import get_user_model
from videos.models import Video

logger = get_logger('notifications')


@shared_task
def add_notiication(user_id: str | int, video_id: str | int, notification_type: str):
    try:
        user = get_user_model().objects.get(id=user_id)
    except:
        logger.error('User does not exist')
        return
    
    try:
        video = Video.objects.get(id=video_id)
    except:
        logger.error('Video does not exist')
        return

    instance = video.notification_set.create(**{
        'user': user,
        'notification_type': notification_type
    })

    return instance.id
