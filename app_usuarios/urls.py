from django.urls import path
from . import views



urlpatterns = [
    path("login/", views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('logout/', views.user_logout, name='logout'),
    path('resetPass/', views.resetPassword, name= 'resetPassword'),

]
