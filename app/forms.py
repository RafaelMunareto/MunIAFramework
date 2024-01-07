# forms.py
from django import forms
from django.core.validators import FileExtensionValidator 

class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='Selecione um arquivo (CSV ou TXT)',
        validators=[FileExtensionValidator(allowed_extensions=['csv', 'txt'])]
    )
    
    file_name = forms.CharField(
        label='Nome do arquivo',
        max_length=255
    )
