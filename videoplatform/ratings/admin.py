from django.contrib import admin

from accounts.sites import custom_admin_site
from ratings.models import Rating


class RatingsAdmin(admin.ModelAdmin):
    list_display = ['video', 'rating_type', 'created_on']
    search_fields = ['video__title', 'video__category']
    date_hierarchy = 'created_on'


custom_admin_site.register(Rating, RatingsAdmin)
