
# from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

class HomePage(TemplateView):
    template_name = 'homePage.html'

