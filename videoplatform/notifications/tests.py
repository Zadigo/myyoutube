from django.test import TestCase, TransactionTestCase, override_settings
from notifications import tasks
from videos.models import Video


@override_settings(CELERY_TASK_ALWAYS_EAGER=True, CELERY_TASK_EAGER_PROPAGATES=True)
class TestTasks(TransactionTestCase):
    fixtures = ['videos']

    @classmethod
    def setUpClass(cls):
        pass

    def test_add_notification(self):
        video = Video.objects.first()

        t1 = tasks.add_notiication.apply(args=(
            video.user.id,
            video.id,
            'Message'
        ))
        result = t1.get()
