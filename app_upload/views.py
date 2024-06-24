from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .models import Folder, File


# _______________FOLDER________________ 

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
            parts = message.message.split(":")
            if len(parts):
                if 'Ficheiro já existe' in message.message:
                    try:
                        error_folder_id = int(parts[-1].strip())
                        error_message = parts[0].strip()
                    except ValueError:
                        pass  
                elif "Pasta renomeada com sucesso" in message.message:
                    try:
                        success_folder_id = int(parts[-1].strip())
                        success_message = parts[0].strip()
                    except ValueError:
                        pass 



    return render(request,'folderView.html', {
        'folders': folders,
        'current_folder_id': current_folder_id,
        'error_folder_id': error_folder_id,
        'error_message': error_message,
        'success_folder_id': success_folder_id,
        'success_message': success_message,
        
        })
        


@login_required(login_url="/login/")
def newFolder (request, folder_id = None): 
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

        
        if Folder.objects.filter(name=foldername, user=user, parent_folder=parent_folder).exists():
            messages.error(request, "Ficheiro já existe")
            return redirect('folderView')

        else:  
            new_folder = Folder(name=foldername, user=user, parent_folder=parent_folder)
            new_folder.save()
            messages.success(request, "Pasta criada")
            return redirect (request.META.get('HTTP_REFERER', 'folderView'))

        

    return redirect('folderView')    

def deleteFolder(request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id)

    if request.method == 'POST':
        folder.delete()
        return redirect('folderView')
    
    return redirect('folderView')


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
        # return redirect('folderView')
        return redirect (request.META.get('HTTP_REFERER', 'folderView'))

    
    return redirect('folderView')



@login_required(login_url="/login/")
def getFolderUrl(request, folder_id):


    current_folder = Folder.objects.get(id=folder_id)
    folders = Folder.objects.filter(user=request.user, parent_folder=current_folder)
    files = File.objects.filter(user=request.user, parent_folder = current_folder)


    return render(request, 'folderContent.html',{
        'folder':current_folder,
        'folders':folders,
        'files':files,
        'current_folder_id': folder_id,
  }) 


# __________________ FILE ____________

@login_required(login_url="/login/")
def uploadFileView(request, folder_id=None):
    user = request.user
    current_folder = None
    error_folder_id = success_folder_id = None
    error_message = success_message = None


    if request.method == 'POST':
        file = request.FILES.get('file')

        if folder_id is not None:
            current_folder = Folder.objects.get(id=folder_id)


        # Confirmando se existe um arquivo para fazer upload e redirecionando para pasta que está
        if not file:
            messages.error(request, "Nenhum arquivo selecionado.")
            if folder_id is None:
                return redirect('folderView') 
            else:
                return redirect('folderParent', folder_id=folder_id)


        try:
            new_file = File(parent_folder=current_folder, user=user, file=file)
            new_file.save()
            messages.success(request, "Arquivo carregado com sucesso")
        except Exception as e:
            messages.error(request, f"Erro ao carregar o arquivo: {str(e)}")


        if folder_id is None:
            return redirect('folderView') 
        else:
            return redirect('folderParent', folder_id=folder_id)


    if messages.get_messages(request):
        for message in messages.get_messages(request):
            parts = message.message.split(":")
            if len(parts):
                if 'Erro ao carregar o arquivo' in message.message:
                    try:
                        error_folder_id = int(parts[-1].strip())
                        error_message = parts[0].strip()
                    except ValueError:
                        pass  
                elif "Arquivo carregado com sucesso" in message.message:
                    try:
                        success_folder_id = int(parts[-1].strip())
                        success_message = parts[0].strip()
                    except ValueError:
                        pass 

    files = File.objects.filter(user=user, parent_folder=current_folder)

    return render(request, 'folderContent.html', {
        'files': files,
        'current_folder_id': folder_id,
        'error_folder_id': error_folder_id,
        'error_message': error_message,
        'success_folder_id': success_folder_id,
        'success_message': success_message,
    })

def deleteFile(request, file_id): 
    file = get_object_or_404(File, id=file_id)

    if request.method == "POST":
        file.delete()
        messages.success(request, "Arquivo deletado com sucesso")

    return redirect(request.META.get('HTTP_REFERER', 'folderView'))


def renameFile (request, file_id):
    file = get_object_or_404(File, id=file_id)

    if request.method == 'POST':
        new_filename = request.POST.get('new_fileName')

        file.file.name=new_filename
        file.save()
        messages.success(request, "Nome do arquivo alterado com sucesso")
    
    return redirect(request.META.get('HTTP_REFERER', 'folderView'))
