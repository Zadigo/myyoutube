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
        choices=choices.SubscriptionModes.choices,
        default='All',
        allow_null=True
    )


class RatingSerializer(Serializer):
    liked = fields.BooleanField(
        default=False
    )
    unliked = fields.BooleanField(
        default=False
    )
    rating_for = fields.ChoiceField(
        choices=choices.RatingFor.choices,
        default='Comment'
    )
    subscription = ValidateSubscription(
        write_only=True
    )

    def create(self, validated_data):
        request = self.context['request']
        video = self.context['video_instance']

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
