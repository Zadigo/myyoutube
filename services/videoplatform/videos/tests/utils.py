from factory.django import DjangoModelFactory
from videos.models import Video
from faker import Faker
from factory.declarations import SubFactory
from accounts.tests.utils import UserFactory

faker = Faker()

class VideoFactory(DjangoModelFactory):
    class Meta:
        model = Video

    user = SubFactory(UserFactory)
    title = faker.sentence(nb_words=4)
    description = faker.paragraph()
    video_id = faker.uuid4()
    video = '/myyoutube/videoplatform/media/test_video.mp4'
