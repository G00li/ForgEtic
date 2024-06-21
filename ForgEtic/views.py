
# from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.urls import reverse


# class LoginCheck(TemplateView):
#     def __init__(self, get_response): 
#         self.get_response = get_response

#     def __call__(self, request):
#         if not request.user.is_authenticated:
#             template_name = 'index.html'
#         elif request.user.is_authenticated and not request.user.is_staff:
#             return redirect('home')
#         elif request.user.is_authenticated and request.user.is_staff:
#                 return redirect(reverse('admin:index'))


class IndexView(TemplateView):
    template_name = 'index.html'


