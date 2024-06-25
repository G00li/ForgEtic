from django.urls import path 
from . import views

urlpatterns = [
    path("", views.folder_view, name="folderView"),
    path("newfolder/", views.newFolder, name="newfolder"),


    path("folderView/<int:folder_id>", views.getFolderUrl, name="folderParent"),
    path('delete_folder/<int:folder_id>', views.deleteFolder, name='delete_folder'),
    path('rename_folder/<int:folder_id>', views.renameFolder, name='rename_folder'),
    path('download_folder/<int:folder_id>', views.downloadFolder, name='download_folder'),

    path('file/upload', views.uploadFileView, name="uploadFile"),
    path('file/upload/<int:folder_id>', views.uploadFileView, name="uploadFile"),

    path('deleteFile/<int:file_id>', views.deleteFile, name ="delete_file"),
    path('rename_file/<int:file_id>', views.renameFile, name ="rename_file"),

  
]
