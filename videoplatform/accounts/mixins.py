from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader


class EmailMixin:
    email_template_name = None
    html_email_template_name = None
    subject_template_name = None

    def send_mail(self, context, to_email):
        from_email = getattr(settings, 'EMAIL_HOST_USER', None)

        # Fail silently if we have 
        # no EMAIL_HOST_USER
        if from_email is not None:
            subject = loader.render_to_string(self.subject_template_name, context)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())

            body = loader.render_to_string(self.email_template_name, context)
            email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
            
            if self.html_email_template_name is not None:
                html_email = loader.render_to_string(
                    self.html_email_template_name, 
                    context
                )
                email_message.attach_alternative(html_email, 'text/html')

            email_message.send()
