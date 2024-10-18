from django.contrib import admin
from stories.models import Story
from accounts.sites import custom_admin_site

# @admin.register(Story)


class StoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'expires', 'is_expired']
    search_fields = ['user__username']
    sortable_by = ['name', 'creaed_on']
    date_hierarchy = 'created_on'


custom_admin_site.register(Story, StoryAdmin)
