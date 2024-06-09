from django.contrib import admin
from django.urls import path, include

from ForgEtic.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='home'),
    path("auth/", include('app_usuarios.urls'), name='usuarios'),
    path("admin/", admin.site.urls),
]
