from django.contrib import admin

from ratings.models import Rating

from accounts.admin import custom_admin
# @admin.register(Rating)


class RatingsAdmin(admin.ModelAdmin):
    list_display = ['rating_type', 'video', 'created_on']
    search_fields = ['video__title', 'video__category']
    date_hierarchy = 'created_on'


custom_admin.register(Rating, RatingsAdmin)
