from notifications import models
from django import template
from django.core.cache import cache

register = template.Library()


@register.simple_tag(takes_context=True)
def total(context):
    user = context['user']
    old_notifications = cache.get('notifications')
    if old_notifications is None:
        notifications = models.Notification.objects.filter(user__id=user.id, read=False)
        cache.set('notifications', notifications.count(), 15)
    return cache.get('notifications')
