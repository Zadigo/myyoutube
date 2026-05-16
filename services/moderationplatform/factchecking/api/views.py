from factchecking.api.serializers import ReportSerializer
from factchecking.models import Report
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from rest_framework.permissions import IsAuthenticated


class CreateReport(CreateAPIView):
    """
    API view to create a new report.
    """
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]


class ListReports(ListAPIView):
    """
    API view to list all reports.
    """
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Report.objects.filter(user=self.request.user)
        return queryset.order_by('-created_on')


class GetUpdateReport(RetrieveUpdateAPIView):
    """
    API view to retrieve and update a specific report.
    """
    queryset = Report.objects.filter(active=True)
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'reference'
