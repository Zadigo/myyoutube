from factory.django import DjangoModelFactory
from faker import Faker
from django.contrib.auth import get_user_model

faker = Faker()

class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = faker.email()
    password = faker.password()
    username = faker.user_name()
    firstname = faker.first_name()
    lastname = faker.last_name()
    is_active = True
