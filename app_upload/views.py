from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



from datetime import datetime

from .models import  Folder ,UploadFile


@login_required(login_url="/login/")

def newFolder (request): 
    if request.method == 'GET':
        return render (request, "folder.html")
    
    elif request.method == 'POST':

        foldername = request.POST.get('foldername')

        newFolder = Folder(name=foldername, user=request.user)
        newFolder.save()
        return redirect ('home')


@login_required(login_url="/login/")
def folder_view(request):
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