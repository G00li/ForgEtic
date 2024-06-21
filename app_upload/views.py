from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import  Folder ,UploadFile
from .forms import UpdateForm
from django.http import HttpResponse


@login_required(login_url="/login/")
def folder_view(request):


    if request.method == 'GET': 
        folders = Folder.objects.filter(user=request.user)
        return render(request,'folderView.html', {'folders': folders})
        

    elif request.method == "POST": 
        return render (request, 'folderView.html')



@login_required(login_url="/login/")
def newFolder (request): 
    if request.method == 'GET':
        return render (request, "folder.html")
    
    elif request.method == 'POST':
        
        foldername = request.POST.get('foldername')
        user = request.user

        if Folder.objects.filter(name=foldername, user=user).exists():
            messages.error(request, "Ficheiro já existe")
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
    user = request.user
    new_name = request.POST.get('new_name')


    if request.method == 'POST':
        if Folder.objects.filter(name=new_name, user=user).exists():
            messages.error(request, "Ficheiro já existe") #TODO - exibir a mensagem de erro no inicio da folder
            return render(request, "folderView.html")
        
        folder.name = new_name
        folder.save()
        return redirect('folderView')
    
    return redirect('folderView.html')





@login_required(login_url="/login/")
def getFolderUrl(request, slug):
    
    folder = request.user.folders.all().filter(id=slug)[0]

    return render(request, 'folderContent.html',{'folder':folder}) 





@login_required(login_url="/login/") 
def uploadFile(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILE)

        if form.is_valid():
            form.save()
            return redirect('uploadSucess')
        
    else:
        form = UpdateForm()

    return render (request, 'upload.html', {'form': form})


def uploadSucess(request):
    return HttpResponse("Upload realizado com sucesso!")