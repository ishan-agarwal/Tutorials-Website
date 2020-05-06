from django import forms
from .models import Tutorial

from tinymce.widgets import TinyMCE

# create a ModelForm 
class UploadForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        fields = "__all__"
