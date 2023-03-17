from django import forms
from .models import *

class NewsForm(forms.ModelForm):
  
    class Meta:
        model = News
        fields = ['title', 'image']