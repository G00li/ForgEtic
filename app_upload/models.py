from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse



class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    # parent = models.ForeignKey("Self", on_delete=models.CASCADE)
    # size = models.FloatField(max_length=100000)


    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(f"{self.id}-{self.name}")
    #     super(Folder,self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    def path_folder(): 
        return reverse("folder", args=[str(id)])



class UploadFile(models.Model): 
    title = models.CharField(max_length = 255)
    file = models.FileField(upload_to = 'files')

    def __str__(self):
        return self.title
    