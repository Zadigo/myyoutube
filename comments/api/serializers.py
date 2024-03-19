from django.utils.translation import gettext_lazy as _
from rest_framework import fields
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

from accounts.api.serializers import UserSerializer
from comments.api.algorithm import text_algorithm
from comments.models import Comment, Reply
from videos.choices import CommentingStrategy


class CommentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'content',
            'from_creator', 'pinned', 'number_of_replies', 'created_on'
        ]


class ReplySerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Reply
        fields = [
            'id', 'user', 'content',
            'from_creator', 'pinned', 'created_on'
        ]


class ValidateCommentSerializer(Serializer):
    content = fields.CharField()

    def save(self, request, video, **kwargs):
        setattr(self, '_request', request)
        setattr(self, '_video', video)
        return super().save(**kwargs)

    def create(self, validated_data):
        if self._video.comment_strategy == CommentingStrategy.DISABLE_ALL:
            raise ValidationError({
                'content': _("Video does not authorize new comments")
            })

        if not self._video.active:
            raise ValidationError(_("Video is not active"))

        validated_text = text_algorithm(validated_data['content'])
        comment = self._video.comment_set.create(
            user=self._request.user,
            content=validated_text
        )

        if self._video.comment_strategy == CommentingStrategy.HOLD_FOR_REVIEW:
            pass

        return comment


class ValidateReplySerializer(Serializer):
    content = fields.CharField()

    # def save(self, request, video, **kwargs):
    #     setattr(self, '_request', request)
    #     setattr(self, '_video', video)
    #     return super().save(**kwargs)

    # def create(self, validated_data):
    #     if self._video.comment_strategy == CommentingStrategy.DISABLE_ALL:
    #         raise ValidationError({
    #             'content': _("Video does not authorize new comments")
    #         })

    #     if not self._video.active:
    #         raise ValidationError(_("Video is not active"))

    #     validated_text = text_algorithm(validated_data['content'])
    #     comment = self._video.comment_set.create(
    #         user=self._request.user,
    #         content=validated_text
    #     )

    #     if self._video.comment_strategy == CommentingStrategy.HOLD_FOR_REVIEW:
    #         pass

    #     return comment
