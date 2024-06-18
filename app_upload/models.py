from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Folder(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    # size = models.FloatField(max_length=100000)

    def __str__(self):
        return self.name
    

    def path_folder(): 
        return reverse("folder", args=[str(id)])



class UploadFile(models.Model): 
    title = models.CharField(max_length = 50)
    file = models.FileField(upload_to = 'files')

    def __str__(self):
        return self.title
    