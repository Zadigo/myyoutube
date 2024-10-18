from accounts.sites import custom_admin_site
from django.contrib import admin
from history.models import History


# @admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['video']
    date_hierarchy = 'created_on'


custom_admin_site.register(History, HistoryAdmin)
