from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60 * 60), name='dispatch')
class GettingStartedView(TemplateView):
    template_name = 'pages/getting_started.html'


@method_decorator(cache_page(60 * 60), name='dispatch')
class EdiitingView(TemplateView):
    template_name = 'pages/getting_started.html'
