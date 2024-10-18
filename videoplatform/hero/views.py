from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name = 'pages/home.html'


@require_POST
def send_message(request, **kwargs):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    send_mail(
        '',
        message=message,
        from_email='',
        recipient_list=[email]
    )
    return JsonResponse(data={})
