
from accounts import forms
from accounts.models import ActivationToken
from django.contrib import auth, messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, RedirectView, View


USER_MODEL = get_user_model()


# @method_decorator(never_cache, name='dispatch')
class SignupView(FormView):
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

    # def get_redirect_url(self, request, intermediate_view=None, user=None):
    #     if intermediate_view is None:
    #         return redirect(request.GET.get('next') or reverse('accounts:profile:home'))
        
    #     if user is None:
    #         return Http404('User could not identified - INT-US')
        
    #     request.session['user'] = user.id
    #     return redirect(intermediate_view)


class LoginView(FormView):
    form_class = forms.UserLoginForm
    template_name = 'pages/registration/login.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return self.form_valid(form)
        # form.add_error(None, error='Account not found')
        return self.form_invalid(form)

        # email = request.POST.get('username')
        # password = request.POST.get('password')

        # user = auth.authenticate(request, email=email, password=password)
        # if user:
        #     auth.login(request, user)
        #     return self.form_valid(form)
        #     # return redirect(request.GET.get('next') or '/')
        # messages.error(request, _("Nous n'avons pas pu trouver votre compte"), extra_tags='alert-danger')
        # return redirect('accounts:login')


class LogoutView(RedirectView):
    url = '/'
    
    def get(self, request, *args, **kwargs):
        url = self.get_redirect_url(*args, **kwargs)
        logout(request)
        return HttpResponseRedirect(url)


class ForgotPasswordView(FormView):
    form_class = forms.CustomPassowordResetForm
    template_name = 'pages/registration/forgot_password.html'
    success_url = reverse_lazy('accounts:forgot_password_reset')

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
    form_class = forms.CustomSetPasswordForm
    template_name = 'pages/registration/forgot_password_reset.html'
    success_url = reverse_lazy('accounts:forgot_password_reset')

    def get_form_kwargs(self):
        params = super().get_form_kwargs()
        # email = self.kwargs.get('email', None)
        # params['user'] = USER_MODEL.objects.filter(email__iexact=email)
        return params

    def post(self, request, **kwargs):
        form = self.get_form()

        if form.is_valid():
            form.save()
            return self.form_valid(form)
        return self.form_invalid(form)


class UnauthenticatedPasswordResetView(View):
    """
    Helps a non authenticated user reset his password
    """
    def get(self, request, *args, **kwargs):
        # user_token = request.GET.get('user_token')
        # if not user_token:
        #     return HttpResponseForbidden(reason='Missing argument')
        
        context = {
            'form': forms.CustomSetPasswordForm(MYUSER.objects.get(id=1)),
        }
        return render(request, 'pages/registration/forgot_password_confirm.html', context)

    def post(self, request, **kwargs):
        # user_token = request.GET.get('user_token')
        # user = get_object_or_404(MYUSER, id=user_token)
        form = forms.CustomSetPasswordForm(user)
        if form.is_valid():
            form.save()
        auth.login(request, user)
        return redirect('profile')


class ActivateAccountView(View):
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
