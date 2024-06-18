from django.urls import path 
from . import views

urlpatterns = [
    path("upload/", views.upload, name="uploadFile"),
    path("newfolder/", views.newFolder, name="newfolder"),
    path("folderView/", views.folder_view, name="folderView"),
    
]


