from django.contrib import admin

from comments.models import Comment, Reply


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_on']
    date_hierarchy = 'created_on'
