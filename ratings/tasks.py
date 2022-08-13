from celery import shared_task

@shared_task
def create_notification(user, instance):
    new_notification = instance.notification_set.create(
        user=user,
        notification_type='Like'
    )
    return new_notification
