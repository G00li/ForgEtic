from django.contrib import admin
from django.urls import path, include

from ForgEtic.views import IndexView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexView.as_view(), name='home'),
    path("auth/", include('app_usuarios.urls'), name='usuarios'),
    path("upload/", include('app_upload.urls'), name = "file"),
    path("admin/", admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
