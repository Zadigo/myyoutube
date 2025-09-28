from django.contrib import admin
from notifications.models import Notification, PreferredNotification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'read']
    date_hierarchy = 'created_on'


@admin.register(PreferredNotification)
class PreferredNotificationAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__email']
