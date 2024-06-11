from django.urls import path
from . import views


urlpatterns = [
    path("", views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('plataforma/', views.homePage, name = 'plataforma') #//NOTE - Apenas para verificar como o decorator @login_required funciona
]
