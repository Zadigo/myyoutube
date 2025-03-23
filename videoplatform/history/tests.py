from django.test import TestCase, override_settings
from history import tasks

@override_settings()
class TestTasks(TestCase):
    fixtures = ['users', 'videos']

    def test_add_video_to_history(self):
        tasks.add_video_to_history.apply(1, 1)
