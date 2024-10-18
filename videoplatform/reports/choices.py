from django.db.models import Choices

class ReportTypes(Choices):
    SEXISM = 'SEXISM'
    RACISM = 'Racism'
