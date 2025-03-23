import cv2
from celery import shared_task
from celery.utils.log import get_logger
from django.contrib.auth import get_user_model
from moviepy import VideoFileClip
from videos.models import Video

logger = get_logger('videos')


@shared_task
def add_new_view(user_id: str | int, video_id: str | int, duration: int | float, ended_at: int | float):
    try:
        instance = Video.objects.get(id=video_id, user__id=user_id)
    except:
        logger.error(f'Video with id: {video_id} does not exist')
        return

    try:
        user = get_user_model().objects.get(id=user_id)
    except:
        logger.error(f'User with id: {video_id} does not exist')
        return

    try:
        instance.mediaview_set.create(
            user=user,
            duration=duration,
            ended_at=ended_at
        )
    except Exception as e:
        logger.error(f'Could not create new view: {e}')


@shared_task
def get_video_metadata(video_id: str | int):
    try:
        instance = Video.objects.get(id=video_id)
    except:
        logger.error(f'Video with id: {video_id} does not exist')
        return

    try:
        metadata = VideoFileClip(str(instance.video.path))
    except:
        logger.error('Video is not a valid format')
        return
    else:
        width, height = metadata.size

        instance.framerate = metadata.fps
        instance.duration = metadata.duration
        instance.width = width
        instance.height = height
        instance.save()
        return instance.id


@shared_task
def get_video_frames(video_id: str | int):
    try:
        instance = Video.objects.get(id=video_id)
    except:
        logger.error(f'Video with id: {video_id} does not exist')
        return

    count = 0
    capture = cv2.VideoCapture(instance.video.path)

    while capture.isOpened():
        if count > k:
            break

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        success, frame = capture.read()

        if not success:
            continue

        cv2.imwrite(f"frame{count}.jpg", frame)
        count = count + 1
