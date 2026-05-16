from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import FormView, TemplateView

from commentsplatform.forms import LoginForm


# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = reverse_lazy('login')


# @method_decorator(cache_page(60 * 15), name='dispatch')
class LoginView(FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    form_class = LoginForm

    def form_valid(self, form):
        # Perform login logic here
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
