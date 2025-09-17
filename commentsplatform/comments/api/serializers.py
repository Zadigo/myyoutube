from django.utils.translation import gettext_lazy as _
from rest_framework import fields
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer

from accounts.api.serializers import UserSerializer
from comments.api.algorithm import text_algorithm
from comments.models import Comment, Reply
from videos.choices import CommentingStrategy
from comments import tasks


class CommentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    user_channel = fields.CharField(read_only=True)
    is_liked = fields.BooleanField(read_only=True, default=False)
    is_disliked = fields.BooleanField(read_only=True, default=False)

    class Meta:
        model = Comment
        fields = [
            'id', 'user', 'content',
            'from_creator', 'pinned',
            'user_channel', 'number_of_replies',
            'is_liked', 'is_disliked',
            'created_on'
        ]

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        request = self.context['request']

        validated_data['user'] = request.user
        validated_data['video'] = self.context['video']

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)

        if self.instance is None:
            raise ValueError('Update or create did not return an object')

        tasks.moderate_comment.apply_async((self.instance.id,), countdown=60)
        return self.instance


class ReplySerializer(ModelSerializer):
    id = fields.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    content = fields.CharField()
    from_creator = fields.BooleanField(read_only=True)
    pinned = fields.BooleanField(read_only=True)
    created_on = fields.DateTimeField(read_only=True)

    class Meta:
        model = Reply
        fields = [
            'id', 'user', 'content',
            'from_creator', 'pinned',
            'created_on'
        ]

    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}

        request = self.context['request']
        validated_data['user'] = request.user
        validated_data['comment'] = self.context['comment']

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
        else:
            self.instance = self.create(validated_data)

        if self.instance is None:
            raise ValueError(
                "Update/create did not "
                "return an object instance"
            )

        tasks.moderate_comment.apply_async((self.instance.id,), countdown=60)
        return self.instance


class ValidateCommentSerializer(Serializer):
    content = fields.CharField()

    def save(self, request, video, **kwargs):
        setattr(self, '_request', request)
        setattr(self, '_video', video)
        return super().save(**kwargs)

    def create(self, validated_data):
        request = self._context['request']

        if self._video.comment_strategy == 'Disable all':
            raise ValidationError({
                'content': _("Video does not authorize new comments")
            })

        if not self._video.active:
            raise ValidationError(_("Video is not active"))

        validated_text = text_algorithm(validated_data['content'])
        comment = self._video.comment_set.create(
            user=request.user,
            content=validated_text
        )

        if self._video.comment_strategy == 'Hold for review':
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
