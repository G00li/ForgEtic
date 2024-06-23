from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import  Folder
from django.db import IntegrityError



@login_required(login_url="/login/")
def folder_view(request, folder_id = None):

    if folder_id:
        parent_folder = Folder.objects.get(id=folder_id)
        folders = Folder.objects.filter(user=request.user, parent_folder= parent_folder)

    else:   
        folders = Folder.objects.filter(user=request.user, parent_folder = None)



    current_folder_id = folder_id
    error_folder_id = success_folder_id = None
    error_message = success_message = None

    if messages.get_messages(request):
        for message in messages.get_messages(request):
            if 'Ficheiro já existe' in message.message:
                error_folder_id = int(message.message.split (":")[-1])
                error_message = message.message.split(":")[0]
            elif "Pasta renomeada com sucesso" in message.message:
                success_folder_id = int(message.message.split (":")[-1])
                success_message = message.message.split(":")[0]



    return render(request,'folderView.html', {
        'folders': folders,
        'current_folder_id': current_folder_id,
        'error_folder_id': error_folder_id,
        'error_message': error_message,
        'success_folder_id': success_folder_id,
        'success_message': success_message,
        
        })
        


@login_required(login_url="/login/")
def newFolder (request): 
    if request.method == 'POST':
        
        foldername = request.POST.get('foldername')
        parent_folder_id = request.POST.get('parent_folder')
        user = request.user

        parent_folder = None
        if parent_folder_id:
            try: 
                parent_folder = Folder.objects.get(id=int(parent_folder_id), user=user)
            except (ValueError,Folder.DoesNotExist):
                parent_folder = None

        else:
            parent_folder = None

        
        if Folder.objects.filter(name=foldername, user=user,parent_folder=parent_folder).exists():
            messages.error(request, "Ficheiro já existe")
            return redirect("folderView")

        else:  
            new_folder = Folder(name=foldername, user=user, parent_folder=parent_folder)
            new_folder.save()
            messages.success(request, "Pasta criada")
        
        return redirect('folderView')
    
    return redirect('folderView')
    

def deleteFolder(request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id)

    if request.method == 'POST':
        folder.delete()
        return redirect('folderView')
    
    return render(request, 'folderView.html')


def renameFolder (request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id, user=request.user)


    if request.method == 'POST':
        new_name = request.POST.get('new_name')

        if Folder.objects.filter(name=new_name, user=folder.user).exists():
            messages.error(request, f"Ficheiro já existe:{folder_id}") 
            return redirect("folderView")
        
        folder.name = new_name
        folder.save()
        messages.success(request, f"Pasta renomeada com sucesso: {folder_id}")
        return redirect('folderView')
    
    return redirect('folderView')



@login_required(login_url="/login/")
def getFolderUrl(request, slug):

    current_folder = Folder.objects.get(id=slug)

    folders = Folder.objects.filter(user=request.user, parent_folder=current_folder)

    return render(request, 'folderContent.html',{
        'folder':current_folder,
        'folders':folders,
        'current_folder_id': slug
  }) 
