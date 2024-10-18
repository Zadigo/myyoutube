from django.contrib import admin

from donations.models import Donation
from accounts.sites import custom_admin_site

# @admin.register(Donation)


class DonationAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_channel', 'value']
    search_fields = ['user__username', 'user_channel__name']
    date_hierarchy = 'created_on'
    actions = ['cancel']

    def cancel(self, queryset):
        queryset.update(cancelled=True)
        return queryset


custom_admin_site.register(Donation, DonationAdmin)
