from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def upload (request): 
    if request.method == 'GET':
        return render(request, "upload.html")
    
    elif request.method == "POST": 
        file = request.FILES

        print(file)

        return HttpResponse("Upload feito") 