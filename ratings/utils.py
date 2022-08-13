from django.conf import settings
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured

def get_notifications_model():
    try:
        model_name = settings.NOTIFICATION_MODEL
    except:
        raise ImproperlyConfigured(
            'Could not load the Notifications model'
        )
    else:
        return apps.get_model(model_name, require_ready=False)
