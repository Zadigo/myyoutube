from accounts import forms
from accounts.models import ActivationToken, MyUser, MyUserProfile
# from django.contrib.auth import admin
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from myadmin.sites import custom_admin


class MyUserAdmin(admin.ModelAdmin):
    form = forms.MyUserChangeForm
    add_form = forms.MyUserCreationForm
    actions = ['activate_account', 'deactivate_account']
    list_display = ['email', 'firstname', 'lastname', 'is_active', 'is_admin']
    list_filter = []
    filter_horizontal = ['groups', 'user_permissions']
    ordering = ['email']
    search_fields = ['firstname', 'lastname', 'email']
    fieldsets = [
        ['Details', {'fields': ['firstname', 'lastname']}],
        ['Credentials', {'fields': ['email', 'password']}],
        ['Permissions', {'fields': ['user_permissions', 'groups',
                                    'is_superuser', 'is_admin', 'is_staff', 'is_active']}]
    ]
    add_fieldsets = [
        [None, {
                'classes': ['wide'],
                'fields': ['email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active']
            }
        ]
    ]
    ordering = ['email']

    def activate_account(self, request, queryset):
        queryset.update(actif=True)

    def deactivate_account(self, request, queryset):
        queryset.update(actif=False)


class MyUserProfileAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'telephone']
    search_fields = ['myuser__firstname', 'myuser__lastname', 'myuser__email']


class ActivateAccountAdmin(admin.ModelAdmin):
    list_display = ['token']


custom_admin.register(ActivationToken, ActivateAccountAdmin)
custom_admin.register(MyUser, MyUserAdmin)
custom_admin.register(MyUserProfile, MyUserProfileAdmin)
custom_admin.register(Group)
