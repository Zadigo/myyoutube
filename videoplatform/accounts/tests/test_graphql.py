
import json

from graphene_django.utils.testing import GraphQLTestCase

from accounts.tests.utils import UserFactory
from accounts.models import CustomUser

class TestVideosGraphQL(GraphQLTestCase):
    def setUp(self):
        self.instance: CustomUser = UserFactory.create()

    def test_get_user(self):
        response = self.query(
            '''
            query($id: String!) {
                getUser(id: $id) {
                    email
                    username
                    firstname
                    lastname
                }
            }
            ''',
            operation_name='getUser',
            variables={
                'id': str(self.instance.id)
            }
        )

        content = json.loads(response.content)
        self.assertResponseNoErrors(response)
