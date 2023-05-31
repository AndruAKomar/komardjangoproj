from django import forms
from . import models
from django.forms import ModelForm

#L
class GenreModelForm(forms.ModelForm):
    class Meta: 
        model = models.Genre
        fields = [
            "name", "description"]