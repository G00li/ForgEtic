from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    parent_folder= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')


    def __str__(self):
        return self.name
    
    def path_folder(): 
        return reverse("folder", args=[str(id)])




