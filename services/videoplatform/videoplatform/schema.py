import graphene
from videos.graphql.schema import VideosQuery
from playlists.schema import PlaylistQuery
from mychannel.graphql.schema import MyChannelQuery
from videos.graphql.mutation import CreateVideoMutation
from playlists.graphql.mutation import CreatePlaylistMutation
from ratings.graphql.mutation import CreateRatingMutation
from ratings.graphql.schema import RatingsQuery
from accounts.graphql.schema import CustomUserQuery, UserProfileQuery, SubscriptionQuery, PreferredAdQuery, ViewingProfileQuery, ActivationTokenQuery
from accounts.graphql.mutation import UpdateViewingProfileMutation
from history.graphql.schema import HistoryQuery

class Query(
    HistoryQuery,
    VideosQuery,
    MyChannelQuery,
    PlaylistQuery,
    RatingsQuery,
    CustomUserQuery,
    UserProfileQuery,
    SubscriptionQuery,
    PreferredAdQuery,
    ViewingProfileQuery,
    ActivationTokenQuery,
    graphene.ObjectType
):
    pass


class Mutation(graphene.ObjectType):
    create_video = CreateVideoMutation.Field()
    create_playlist = CreatePlaylistMutation.Field()
    create_rating = CreateRatingMutation.Field()
    update_viewing_profile = UpdateViewingProfileMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
