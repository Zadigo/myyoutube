from accounts.admin import custom_admin
from django.contrib import admin
from history.models import History


# @admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['video']
    date_hierarchy = 'created_on'


custom_admin.register(History, HistoryAdmin)
