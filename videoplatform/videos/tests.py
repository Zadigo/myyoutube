from django.test import TransactionTestCase
from django.core.serializers import serialize


class TestVideoApiResponse(TransactionTestCase):
    fixtures = ['videos']

    @classmethod
    def setUpTestData(cls):
        pass

    def test_video_categories(self):
        pass

    def test_video_subcategories(self):
        pass

    def test_list_videos(self):
        pass

    def test_upload_video(self):
        pass

    def test_get_video(self):
        pass

    def test_viewing_profile(self):
        pass

    def test_list_user_videos(self):
        pass


class TestCommentApiResponse(TransactionTestCase):
    def test_create_comment(self):
        pass


class TestTasks(TransactionTestCase):
    pass
