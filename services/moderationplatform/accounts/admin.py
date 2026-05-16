from django.contrib import admin
from accounts.models import ModerationUser


@admin.register(ModerationUser)
class ModerationUserAdmin(admin.ModelAdmin):
    list_diplay = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']
    ordering = ['username']
    readonly_fields = ['username', 'youtube_id', 'password', 'email', 'first_name', 'last_name']
    filter_horizontal = ['groups', 'user_permissions']
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'youtube_id')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )
