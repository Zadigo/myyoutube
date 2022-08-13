from django.contrib import admin
from notifications import models

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
