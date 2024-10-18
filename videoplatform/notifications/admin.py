from django.contrib import admin
from notifications.models import Notification
from accounts.sites import custom_admin_site


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'read']
    date_hierarchy = 'created_on'


custom_admin_site.register(Notification, NotificationAdmin)
