from django.urls import path
from . import views



urlpatterns = [
    path("login/", views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('logout/', views.user_logout, name='logout'),
    path('plataforma/', views.homePage, name = 'plataforma'), #//NOTE - Apenas para verificar como o decorator @login_required funciona
    path('resetPass/', views.resetPassword, name= 'resetPassword'),

]
