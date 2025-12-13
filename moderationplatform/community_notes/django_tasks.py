from community_notes.models import CommunityNote
from django.db.models import F
from django.tasks import task


@task
def apply_vote(noteid: int, value: int):
    if value == 1:
        CommunityNote.objects.filter(pk=noteid).update(
            upvotes=F('upvotes') + 1,
            score=F('score') + 1
        )
    else:
        CommunityNote.objects.filter(pk=noteid).update(
            downvotes=F('downvotes') + 1,
            score=F('score') - 1
        )
