from rest_framework import fields
from rest_framework.serializers import Serializer
from rest_framework.exceptions import ValidationError
from ratings import choices
from ratings.models import Rating


class ValidateSubscription(Serializer):
    subscribed = fields.BooleanField(
        default=False
    )
    mode = fields.ChoiceField(
        choices.SubscriptionModes.choices,
        allow_null=True
    )


class ValidateRating(Serializer):
    liked = fields.BooleanField(
        default=False
    )
    unliked = fields.BooleanField(
        default=False
    )
    subscription = ValidateSubscription()

    def save(self, request, video, **kwargs):
        setattr(self, 'request', request)
        setattr(self, 'video_instance', video)
        return super().save(**kwargs)

    def create(self, validated_data):
        request = getattr(self, 'request')
        video_instance = getattr(self, 'video_instance')
        params = {
            'user': request.user,
            'video': video_instance,
            'rating_for': 'Video'
        }

        if validated_data['liked'] and validated_data['unliked']:
            raise ValidationError('Invalid data for rating')

        if validated_data['liked']:
            params['rating_type'] = 'Like'
        
        if validated_data['unliked']:
            params['rating_type'] = 'Dislike'

        return Rating.objects.create(**params)

    def update(self, instance, validated_data):
        if not validated_data['liked'] and not validated_data['unliked']:
            return instance

        if validated_data['liked']:
            instance.rating_type = 'Like'

        if validated_data['unliked']:
            instance.rating_type = 'Dislike'

        return instance
