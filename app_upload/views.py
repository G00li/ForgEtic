from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from datetime import datetime
from .models import  Folder ,UploadFile


@login_required(login_url="/login/")
def newFolder (request): 
    if request.method == 'GET':
        return render (request, "folder.html")
    
    elif request.method == 'POST':
        
        foldername = request.POST.get('foldername')
        user = request.user


        if Folder.objects.filter(name=foldername, user=user).exists():
            messages.error(request, "Folder already exists")
            return render(request, "folder.html")

        newFolder = Folder(name=foldername, user=request.user)
        newFolder.save()
        return redirect ('folderView')
    

def deleteFolder(request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id)

    if request.method == 'POST':
        folder.delete()
        return redirect('folderView')
    
    return render(request, 'folderView.html')


def renameFolder (request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        folder.name = new_name
        folder.save()
        return redirect('folderView')
    
    return render (request, 'folderView.html')





@login_required(login_url="/login/")
def getFolderUrl(request, slug):
    
    folder = request.user.folders.all().filter(id=slug)[0]

    return render(request, 'folderContent.html',{'folder':folder}) 




@login_required(login_url="/login/")
def folder_view(request):
    # print(request.user.folders.all().filter(name='leandro')[0].id)

    
    if request.method == 'GET': 
        folders = Folder.objects.filter(user=request.user)
        return render(request,'folderView.html', {'folders': folders})
        

    elif request.method == "POST": 
        return render (request, 'folderView.html')



current_time = datetime.now()
@login_required(login_url="/login/") 
def upload (request): 
    if request.method == 'GET':
        return render(request, "upload.html")
    
    elif request.method == "POST": 
        file = request.FILES.get('upload_file')


        uploadFile = UploadFile(title = "File", file=file)
        uploadFile.save()

        return redirect ('home')