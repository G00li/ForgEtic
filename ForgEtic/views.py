
# from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import reverse


class IndexView(TemplateView):
    template_name = 'index.html'


