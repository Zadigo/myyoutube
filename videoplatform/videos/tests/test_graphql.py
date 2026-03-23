
from graphene_django.utils.testing import GraphQLTestCase

class TestVideosGraphQL(GraphQLTestCase):
    def test_get_all_videos(self):
        response = self.query(
            '''
            query {
                allVideos {
                    edges {
                    node {
                        id
                        title
                        tags {
                        id
                        name
                        }
                    }
                    }
                }
            }
            ''',
            operation_name='allVideos'
        )

        print(response.content)
        # content = json.loads(response.content)
        # self.assertResponseNoErrors(response, response.content)
