from django.urls import path 
from . import views

urlpatterns = [
    path("", views.folder_view, name="folderView"),
    path("newfolder/", views.newFolder, name="newfolder"),


    # path("folderView/", views.folder_view, name="folderView"),
    path("folderView/<slug:slug>", views.getFolderUrl, name="folderParent"),
    path('delete_folder/<int:folder_id>', views.deleteFolder, name='delete_folder'),
    path('rename_folder/<int:folder_id>', views.renameFolder, name='rename_folder'),

  
]
