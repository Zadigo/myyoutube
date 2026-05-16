from django.contrib import admin
from ratings.models import Rating


@admin.register(Rating)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ['rating_type', 'created_on']
    search_fields = ['comment__text', 'comment__user__username']
    date_hierarchy = 'created_on'
