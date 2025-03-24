from celery import shared_task


@shared_task
def moderate_comment(instance_id: int):
    pass
