from django.contrib import admin
from notifications.models import Notification
from accounts.admin import custom_admin


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'read']
    date_hierarchy = 'created_on'


custom_admin.register(Notification, NotificationAdmin)
