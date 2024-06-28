from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.utils.http import unquote

from django.contrib import messages
from .models import Folder, File
import os 
import zipfile


from django.conf import settings
from django.utils.text import slugify

from ForgEtic.middlewares import block_superuser




# _______________FOLDER________________ 

@block_superuser
@login_required(login_url="/login/")
def folder_view(request, folder_id = None):

    user = request.user

    # Dentro de outra folder
    if folder_id:
        parent_folder = get_object_or_404(Folder, id=folder_id, user=user)
        folders = Folder.objects.filter(user=user, parent_folder= parent_folder)
        files = File.objects.filter(user=user, parent_folder=parent_folder)

    # Na root do projeto 
    else:   
        folders = Folder.objects.filter(user=user, parent_folder = None)
        files = File.objects.filter(user=user, parent_folder=None)
        



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



    context = {
        'folders': folders,
        'files': files,
        'current_folder_id': current_folder_id,
        'error_folder_id': error_folder_id,
        'error_message': error_message,
        'success_folder_id': success_folder_id,
        'success_message': success_message,
        
        }
    
    return render(request, 'folderView.html', context)
        

@block_superuser
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

        
        if Folder.objects.filter(name=foldername, user=user, parent_folder=parent_folder).exists():
            messages.error(request, "Ficheiro já existe")
            return redirect (request.META.get('HTTP_REFERER', 'folderView'))

        else:  
            new_folder = Folder(name=foldername, user=user, parent_folder=parent_folder)
            new_folder.save()
            messages.success(request, "Pasta criada")
            return redirect (request.META.get('HTTP_REFERER', 'folderView'))

        

    return redirect (request.META.get('HTTP_REFERER', 'folderView'))   


@block_superuser
def deleteFolder(request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id)

    if request.method == 'POST':
        folder.delete()
        messages.success(request, "Pasta deletada com sucesso")
        return redirect (request.META.get('HTTP_REFERER', 'folderView'))
    
    return redirect('folderView')


@block_superuser
def renameFolder (request, folder_id):

    folder = get_object_or_404(Folder, pk=folder_id, user=request.user)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')

        if Folder.objects.filter(name=new_name, user=folder.user).exists():
            messages.error(request, f"Ficheiro já existe.") 
            return redirect (request.META.get('HTTP_REFERER', 'folderView'))

        
        folder.name = new_name
        folder.save()
        messages.success(request, f"Pasta renomeada com sucesso.")
        return redirect (request.META.get('HTTP_REFERER', 'folderView'))

    
    return redirect('folderView')


@block_superuser
@login_required(login_url="/login/")
def downloadFolder(request, folder_id): 
    current_folder = get_object_or_404(Folder, id=folder_id, user =request.user)

    def generate_file_path(folder):
        file_paths = []

        for file in File.objects.filter(parent_folder=folder):
            file_paths.append(file.file.path)

        for subfolder in folder.subfolders.all():
            file_paths.extend(generate_file_path(subfolder))
    
        return file_paths
    
    file_paths = generate_file_path(current_folder)

    zip_filename = f"{current_folder.name}.zip"
    zip_filepath = os.path.join(settings.MEDIA_ROOT, zip_filename)


    with zipfile.ZipFile(zip_filepath, 'w') as zipf:

        for path in file_paths:
            zipf.write(path, os.path.relpath(path, settings.MEDIA_ROOT))

    zip_file = open (zip_filepath, 'rb')
    response = FileResponse(zip_file, content_type = 'application/zip')
    response['Content-Disposition'] = f'attachment; filename={unquote(zip_filename)}'

    return response


# Gerando a url para quando está dentro de uma pasta
@block_superuser
@login_required(login_url="/login/")
def getFolderUrl(request, folder_id):


    current_folder = Folder.objects.get(id=folder_id)
    folders = Folder.objects.filter(user=request.user, parent_folder=current_folder)
    files = File.objects.filter(user=request.user, parent_folder = current_folder)

    folder_path = get_folder_path(current_folder)

    return render(request, 'folderContent.html',{
        'folder':current_folder,
        'folders':folders,
        'files':files,
        'current_folder_id': folder_id,
        'folder_path': folder_path,
    }) 


# Busca o caminho desde a root até a folder atual
def get_folder_path(folder):
    path = []
    current_folder = folder
    while current_folder:
        path.insert(0, current_folder)
        current_folder = current_folder.parent_folder
    return path


# __________________ FILE ____________
@block_superuser
@login_required(login_url="/login/")
def uploadFileView(request, folder_id=None):
    user = request.user
    current_folder = None
    files = File.objects.filter(user=user, parent_folder=current_folder)


    if request.method == 'POST':

        files = request.FILES.getlist('files')

        if folder_id is not None:
            current_folder = Folder.objects.get(id=folder_id)


        # Confirmando se existe um arquivo para fazer upload e redirecionando para pasta que está
        if not files:
            messages.error(request, "Nenhum arquivo selecionado.")
            if folder_id is None:
                return redirect('folderView') 
            else:
                return redirect('folderParent', folder_id=folder_id)

        for file in files: 
            try:
                base_filename, extension = os.path.splitext(file.name)

                slug = slugify(base_filename)
                count = 1
                new_filename = f"{slug}{extension}"



                while File.objects.filter(parent_folder = current_folder, user = user, name=new_filename).exists():
                    new_filename = f"{slug}{count}{extension}"
                    count = count + 1


                new_file = File(parent_folder=current_folder, user=user, file=file, name=new_filename)
                new_file.file.name = new_filename
                new_file.save()

                messages.success(request, "Arquivo carregado com sucesso")
            
            
            except Exception as e:
                messages.error(request, f"Erro ao carregar o arquivo: {str(e)}")


        if folder_id is None:
            return redirect('folderView') 
        else:
            return redirect('folderParent', folder_id=folder_id)

@block_superuser
@login_required(login_url="/login/")
def deleteFile(request, file_id): 
    file = get_object_or_404(File, id=file_id)

    if request.method == "POST":
        file.file.delete()
        file.delete()
        messages.success(request, "Arquivo deletado com sucesso")

    return redirect(request.META.get('HTTP_REFERER', 'folderView'))

@block_superuser
@login_required(login_url="/login/")
def renameFile (request, file_id):
    file = get_object_or_404(File, id=file_id)

    if request.method == 'POST':

        new_filename_base = request.POST.get('new_fileName')

        base_filename, extension = os.path.splitext(file.file.name)
        
        new_filename = f"{new_filename_base}{extension}"



        if File.objects.filter(name=new_filename, user=file.user).exists():
            messages.error(request, f"Arquivo já existe:{new_filename}")
            return redirect(request.META.get('HTTP_REFERER', 'folderView'))
        else:
            file.name=new_filename
            file.save()
            messages.success(request, "Nome do arquivo alterado com sucesso")
    
    return redirect(request.META.get('HTTP_REFERER', 'folderView'))
