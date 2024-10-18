from django.contrib import admin

from accounts.sites import custom_admin_site
from comments.models import Comment, Reply


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'


class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'


custom_admin_site.register(Comment, CommentAdmin)
custom_admin_site.register(Reply, ReplyAdmin)
