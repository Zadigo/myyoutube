from celery import shared_task


@shared_task
def verify_source(url: str):
    return
