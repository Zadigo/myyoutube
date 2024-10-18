from django.contrib import admin
from reports.models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['reference', 'category', 'reviewed_by', 'reviewed']
    search_fields = ['video__title', 'reviewed_by__username']
    date_hierarchy = 'reviewed_on'
    actions = ['report_completed']

    def report_completed(self, queryset):
        return queryset.update(reviewed=True)
