from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.core.exceptions import ValidationError

class CustomAdminAuthenticationForm(AdminAuthenticationForm):
    def clean(self):
        # The field comes as "username" even
        # though we are using the email field
        # for authentication
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request,
                email=email,
                password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise ValidationError(
                self.error_messages['invalid_login'],
                code='invalid_login',
                params={'email': self.username_field.verbose_name},
            )


class CustomAdminSite(AdminSite):
    login_form = CustomAdminAuthenticationForm
    # @never_cache
    # def login(self, request, extra_context=None):
    #     if request.method == 'GET' and self.has_permission(request):
    #         index_path = reverse('admin:index', current_app=self.name)
    #         return HttpResponseRedirect(index_path)

    #     from django.contrib.auth.views import LoginView

    #     context = {
    #         **self.each_context(request),
    #         'title': _("Log in"),
    #         'app_path': request.get_full_path(),
    #         'username': request.uer.get_username()
    #     }

    #     if (REDIRECT_FIELD_NAME not in request.GET and
    #             REDIRECT_FIELD_NAME not in request.POST):
    #         context[REDIRECT_FIELD_NAME] = reverse(
    #             'admin:index', current_app=self.name)
    #     context.update(extra_context or {})

    #     defaults = {
    #         'extra_context': context,
    #         'authentication_form': self.login_form or CustomAdminAuthenticationForm,
    #         'template_name': self.login_template or 'admin/login.html',
    #     }
    #     request.current_app = self.name
    #     return LoginView.as_view(**defaults)(request)


# class DefaultAdminSite(LazyObject):
#     def _setup(self):
#         AdminSiteClass = import_string(apps.get_app_config("admin").default_site)
#         self._wrapped = AdminSiteClass()

#     def __repr__(self):
#         return repr(self._wrapped)


# site = DefaultAdminSite()
custom_admin = CustomAdminSite()
