from django.contrib import admin
from history.models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['video']
