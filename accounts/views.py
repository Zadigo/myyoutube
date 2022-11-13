
from accounts import forms
from accounts.models import ActivationToken
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView, View
from accounts.mixins import EmailMixin

USER_MODEL = get_user_model()


@method_decorator(never_cache, name='dispatch')
@method_decorator(sensitive_post_parameters('password'), name='dispatch')
class SignupView(FormView):
    """Signup user"""
    form_class = forms.UserSignupForm
    template_name = 'pages/registration/signup.html'
    success_url = reverse_lazy('accounts:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        message = {
            'level': messages.ERROR,
            'extra_tags': 'alert-danger'
        }
        if form.is_valid():
            email = form.cleaned_data['email']
            user = USER_MODEL.objects.filter(email__iexact=email)

            if user.exists():
                message.update({'message': _("You already have an account")})
                return self.form_valid(form)

            new_user = form.save()
            if new_user:
                return self.form_valid(form)

        message.update({'message': _("An error occured - SIG-ER")})
        messages.add_message(request, **message)
        return self.form_invalid(form)


@method_decorator(never_cache, name='dispatch')
@method_decorator(sensitive_post_parameters('password'), name='dispatch')
class LoginView(EmailMixin, FormView):
    """Login user"""
    form_class = forms.UserLoginForm
    template_name = 'pages/registration/login.html'
    success_url = '/'
    html_email_template_name = 'emails/welcome.html'
    subject_template_name = 'emails/welcome.txt'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                self.send_mail({}, user.email)
                return self.form_valid(form)
        return self.form_invalid(form)


class LogoutView(RedirectView):
    """Logout user"""
    url = '/'

    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(*args, **kwargs)
        logout(request)
        return HttpResponseRedirect(url)


class ForgotPasswordView(FormView):
    """Enter email address to reset
    password"""
    form_class = forms.CustomPassowordResetForm
    template_name = 'pages/registration/forgot_password.html'
    success_url = reverse_lazy('accounts:login')

    def post(self, request, **kwargs):
        form = self.get_form()

        if form.is_valid():
            email = form.cleaned_data['email']
            user = USER_MODEL.objects.filter(email__iexact=email)

            if user.exists():
                form.save(request, email)
                return self.form_valid(form)
        form.add_error(None, 'Could not find')
        return self.form_invalid(form)


class ForgotPasswordResetView(FormView):
    """Enter new passwords to reset account"""
    form_class = forms.CustomSetPasswordForm
    template_name = 'pages/registration/forgot_password_reset.html'
    success_url = reverse_lazy('accounts:login')

    def get_form_kwargs(self):
        params = super().get_form_kwargs()
        uid = self.kwargs['uidb64']
        token = self.kwargs['token']
        user = get_object_or_404(
            USER_MODEL, 
            id=urlsafe_base64_decode(uid).decode()
        )
        if not default_token_generator.check_token(user, token):
            raise Http404('Token not valid')
        params['user'] = user
        return params

    def post(self, request, **kwargs):
        form = self.get_form()

        if form.is_valid():
            user = form.save()
            user.send_mail()
            return self.form_valid(form)
        return self.form_invalid(form)


class ActivateAccountView(EmailMixin, View):
    """Activate account"""
    def get(self, request, token, *args, **kwargs):
        context = {'is_active': False}
        token_object = get_object_or_404(ActivationToken, token=token)

        if not token_object.myuser.is_active:
            if token_object.is_valid:
                token_object.myuser.is_active = True
                token_object.myuser.save()
                token_object.delete()
                context.update(is_active=True)
        return render(request, 'pages/registration/activate.html', context)


# class UnauthenticatedPasswordResetView(View):
#     """Helps a non authenticated user reset his password"""
#     def get(self, request, *args, **kwargs):
#         # user_token = request.GET.get('user_token')
#         # if not user_token:
#         #     return HttpResponseForbidden(reason='Missing argument')

#         context = {
#             'form': forms.CustomSetPasswordForm(MYUSER.objects.get(id=1)),
#         }
#         return render(request, 'pages/registration/forgot_password_confirm.html', context)

#     def post(self, request, **kwargs):
#         # user_token = request.GET.get('user_token')
#         # user = get_object_or_404(MYUSER, id=user_token)
#         form = forms.CustomSetPasswordForm(user)
#         if form.is_valid():
#             form.save()
#         auth.login(request, user)
#         return redirect('profile')
