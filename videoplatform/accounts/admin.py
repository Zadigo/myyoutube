from accounts import forms
from accounts.models import ActivationToken, CustomUser, UserProfile
from accounts.sites import custom_admin_site
from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from import_export import resources


class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserCreationForm
    add_form_template = 'admin/auth/user/add_form.html'
    change_password_form = AdminPasswordChangeForm
    resource_classes = [CustomUserResource]
    actions = ['activate_account', 'deactivate_account']
    list_display = ['email', 'firstname', 'lastname', 'is_active', 'is_admin']
    list_filter = []
    filter_horizontal = ['groups', 'user_permissions']
    ordering = ['email']
    search_fields = ['firstname', 'lastname', 'email']
    fieldsets = [
        [
            'Details', {
                'fields': ['firstname', 'lastname']
            }
        ],
        [
            'Credentials', {
                'fields': ['email', 'password']
            }
        ],
        [
            'Permissions', {
                'fields': [
                    'user_permissions',
                    'groups',
                    'is_superuser',
                    'is_admin',
                    'is_staff',
                    'is_active'
                ]
            }
        ]
    ]
    add_fieldsets = [
        [
            None, {
                'classes': ['wide'],
                'fields': [
                    'email',
                    'password1',
                    'password2',
                    'is_admin',
                    'is_staff',
                    'is_active'
                ]
            }
        ]
    ]
    ordering = ['email']

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """Use special form for user creation"""
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def activate_account(self, request, queryset):
        queryset.update(actif=True)

    def deactivate_account(self, request, queryset):
        queryset.update(actif=False)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['myuser', 'telephone']
    search_fields = ['customuser__firstname',
                     'customuser__lastname', 'customuser__email']


class ActivateAccountAdmin(admin.ModelAdmin):
    list_display = ['token']


custom_admin_site.register(ActivationToken, ActivateAccountAdmin)
custom_admin_site.register(CustomUser, UserProfile)
custom_admin_site.register(UserProfile, UserProfileAdmin)
