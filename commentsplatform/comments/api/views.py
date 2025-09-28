from django.db.models import Q, Case, When
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from comments.api import serializers
from comments.models import Comment


class ListComments(GenericAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = []
    lookup_field = 'reference'
    lookup_url_kwarg = 'video_id'

    def get(self, request, video_id, *args, **kwargs):
        sort_descending = request.GET.get('desc', 'true')
        video = get_object_or_404(Comment, video_id=video_id)

        fields = ['-id', '-created_on']
        if sort_descending != 'true':
            fields = ['id', 'created_on']

        comments = video.comment_set.select_related('user').order_by(*fields)
        if self.request.user.is_authenticated:
            liked = When(Q(rating__user=self.request.user,
                         rating__rating_type='Like'), then=True)
            disliked = When(Q(rating__user=self.request.user,
                            rating__rating_type='Dislike'), then=True)

            case1 = Case(liked, default=False)
            case2 = Case(disliked, default=False)

            comments = comments.annotate(is_liked=case1, is_disliked=case2)

        comments_as_values = comments.values(
            'id',
            'user__userchannel__reference'
        )

        # Add the channel reference to the comments
        # which will then allow use to get the channel
        # for each commenting user in the frontend
        serializer = self.get_serializer(instance=comments, many=True)

        remapped_comments = []
        for item in serializer.data:
            comment = comments_as_values.get(id=item['id'])
            item['user_channel'] = comment['user__userchannel__reference']
            remapped_comments.append(item)

        return Response(remapped_comments)


class CreateReply(CreateAPIView):
    serializer_class = serializers.ReplySerializer
    queryset = Comment.objects.all()
    permission_classes = []

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['comment'] = self.get_object()
        return context
