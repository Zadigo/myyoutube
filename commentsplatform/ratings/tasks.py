import requests
from celery import shared_task


@shared_task
def create_notification(user_id: int, comment_id: int = None, reply_id: int = None):
    pass


@shared_task
def compute_likes_dislikes(video_id: str):
    pass
