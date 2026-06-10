from rest_framework import fields
from rest_framework.serializers import Serializer
from rest_framework.exceptions import ValidationError
from ratings import choices
from ratings.models import Rating
from videos.api.serializers import VideoSerializer


class RatingSeralizer(Serializer):
    id = fields.IntegerField()
    rating_type = fields.CharField()
    rating_for = fields.CharField()
    video = VideoSerializer()


class ValidateSubscription(Serializer):
    subscribed = fields.BooleanField(
        default=False
    )
    mode = fields.ChoiceField(
        choices.SubscriptionModes.choices,
        default='All',
        allow_null=True
    )


class BaseValidateRating(Serializer):
    liked = fields.BooleanField(
        default=False
    )
    unliked = fields.BooleanField(
        default=False
    )
    rating_for = fields.CharField(default='Video')
    subscription = ValidateSubscription(write_only=True)

    def validate_rating_for(self, value):
        rating_types = list(map(
            lambda x: x[0],
            choices.RatingFor.choices
        ))

        if value not in rating_types:
            raise ValidationError('Invalid rating for')
        return value

    def create(self, validated_data):
        request = self._context['request']
        video = self._context['video_instance']

        logic = any([
            not video.active,
            video.visibility == 'Private'
        ])

        if logic:
            raise ValidationError('Video is not available for rating')

        params = {
            'user': request.user,
            'video': video,
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
        if not validated_data['liked'] and not validated_data['unlinked']:
            return instance

        if validated_data['liked']:
            instance.rating_type = 'Like'

        if validated_data['unliked']:
            instance.rating_type = 'Dislike'

        instance.save()
        return instance
