from django.contrib import admin
from accounts.admin import custom_admin

from comments.models import Comment, Reply


# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'


# @admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'


custom_admin.register(Comment, CommentAdmin)
custom_admin.register(Reply, ReplyAdmin)
