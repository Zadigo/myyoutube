from django.db import models
from django.utils.translation import gettext_lazy as _


class NoteStatus(models.TextChoices):
    DRAFT = 'draft', _('Draft')
    PENDING = 'pending', _('Pending review')
    APPROVED = 'approved', _('Approved')
    REJECTED = 'rejected', _('Rejected')
    FLAGGED = 'flagged', _('Flagged')
