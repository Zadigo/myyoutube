from django.shortcuts import render
from django.views.generic import ListView

from reports.models import Report


class UserReportsView(ListView):
    model = Report
    template_name = 'pages/reports.html'
    context_object_name = 'reports'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
