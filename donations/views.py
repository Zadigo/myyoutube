from django.contrib.messages.api import error
from django.db.transaction import atomic
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from donations.models import Donation
from mychannel.models import UserChannel
from notifications.models import Notification
from videos.models import Video


@method_decorator(cache_page(15 * 60), name='dispatch')
class MyDonations(ListView):
    model = Donation
    template_name = 'pages/donations.html'
    context_object_name = 'donations'

    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user
        )


@atomic
@require_POST
def send_donation(request, **kwargs):
    channel_reference = request.POST.get('channel', None)
    video_reference = request.POST.get('video')
    value = request.POST.get('value', None)

    if channel_reference is not None and value is not None:
        channel = get_object_or_404(UserChannel, reference=channel_reference)
        video = get_object_or_404(Video, reference=video_reference)

        details = {
            'user': request.user,
            'user_channel': channel,
            'value': value
        }

        # Check if the user has made donations
        # within a specific time frame and if
        # the amount of donations exceeds a certain
        # count, block this new donation
        # donations = Donation.objects.filter(
        #     created_on__gt=None, created_on__lt=None
        # )
        # if donations.exists():
        #     if donations.count() > 5:
        #         return JsonResponse(data={'state': False, 'reason': 'exceeded'})

        new_donation = Donation.objects.create(**details)
        if new_donation:
            details = {
                'video': video,
                'notification_type': 'Donation'
            }
            notifications_to_send = [
                Notification(user=request.user, **details),
                Notification(user=channel.user, **details),
            ]
            Notification.objects.bulk_create(notifications_to_send)
    else:
        error(request, 'An error occured - DON-NR', extra_tags='alert-danger')
    return JsonResponse(data={})


@atomic
@require_POST
def cancel_donation(request, **kwargs):
    pass
