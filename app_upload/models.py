from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    parent_folder= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')
    


    def __str__(self):
        return self.name
    
    def path_folder(self): 
        return reverse("folder", args=[self.id])



class File (models.Model):
    name = models.CharField(max_length=50, default='')
    file = models.FileField(upload_to="", blank=False, verbose_name="file")
    user = models.ForeignKey(User, blank= False, on_delete=models.CASCADE, verbose_name="file_User")
    parent_folder = models.ForeignKey(Folder, blank=True, null=True, on_delete=models.CASCADE, verbose_name= "parent_folder")

    def __str__(self):
        return self.file.name
