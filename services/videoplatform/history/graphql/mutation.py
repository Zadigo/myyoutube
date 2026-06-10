import graphene
from history import tasks

class CreateHistoryMutation(graphene.Mutation):
    class Arguments:
        video_id = graphene.ID(required=True)
    
    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, video_id):
        user = info.context.user
        if user.is_authenticated:
            tasks.add_video_to_history.apply_async(args=[user.id, video_id], countdown=10)
            return CreateHistoryMutation(success=True)
        return CreateHistoryMutation(success=False)
