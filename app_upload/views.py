from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import  UploadFile


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