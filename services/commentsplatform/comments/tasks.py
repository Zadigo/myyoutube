from celery import shared_task


@shared_task
def create_comment(video_id: str, user_id: str, content: str):
    pass


@shared_task
def create_reply(video_id: str, user_id: str, content: str, parent_comment_id: int = None):
    pass


@shared_task
def moderate(comment_id: int = None, reply_id: int = None):
    pass
