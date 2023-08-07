from django import forms
from .models import *

class AddFactForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = '__all__'