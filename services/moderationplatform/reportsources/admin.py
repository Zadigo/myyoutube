from django.contrib import admin
from reportsources.models import ReportSource


@admin.register(ReportSource)
class ReportSourceAdmin(admin.ModelAdmin):
    list_display = ['reference', 'url', 'source_credibility', 'created_on']
    search_fields = ['reference', 'url']
    list_filter = ['source_credibility', 'created_on', 'updated_on']
    ordering = ['-created_on']
    readonly_fields = ['created_on', 'updated_on', 'reference']
