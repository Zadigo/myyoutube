from django.db import transaction
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from videos.models import Video
from django.views.generic import ListView
from comments.models import Comment
from django.contrib import messages

class CommentsView(ListView):
    model = Comment
    template_name = 'pages/comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = self.model.objects.filter(
            user=self.request.user
        )
        return queryset

@require_POST
def new_comment(request, **kwargs):
    data = {'state': False}
    reference = request.POST.get('reference', None)
    content = request.POST.get('comment', None)
    if reference is not None:
        video = get_object_or_404(Video, reference=reference)
        new_comment = video.comment_set.create(
            user=request.user,
            content=content
        )
        data.update({'state': True, 'comment': new_comment.content})
    return JsonResponse(data=data)


@require_POST
@transaction.atomic
def new_reply(request, **kwargs):
    data = {'state': False}
    reference = request.POST.get('reference', None)
    reply = request.POST.get('reply', None)
    comment_id = request.POST.get('comment_id', None)
    if comment_id is not None:
        if comment_id.isnumeric():
            comment_id = int(comment_id)
        if reference is not None:
            video = get_object_or_404(Video, reference=reference)
            comment = video.comment_set.get(id=comment_id)
            reply = comment.reply_set.create(user=request.user, content=reply)
            data.update({'state': True, 'content': reply.content})
    else:
        messages.error(request, message='An error occured - REP-NC', extra_tags='alert-danger')
    return JsonResponse(data=data)
