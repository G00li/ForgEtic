from django import forms
from .models import UploadFile


class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = UploadFile
        fields = ('title', 'file')