from django.contrib import admin
from notifications.models import Notification, PreferredNotification
from accounts.sites import custom_admin_site


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'read']
    date_hierarchy = 'created_on'


class PreferredNotificationAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__email']


custom_admin_site.register(Notification, NotificationAdmin)
custom_admin_site.register(PreferredNotification, PreferredNotificationAdmin)
