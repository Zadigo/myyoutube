from django.contrib import admin

from donations.models import Donation
from accounts.admin import custom_admin

# @admin.register(Donation)


class DonationAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_channel', 'value']
    search_fields = ['user__username', 'user_channel__name']
    date_hierarchy = 'created_on'
    actions = ['cancel']

    def cancel(self, queryset):
        queryset.update(cancelled=True)
        return queryset


custom_admin.register(Donation, DonationAdmin)
