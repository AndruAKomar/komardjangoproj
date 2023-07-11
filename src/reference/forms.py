from django import forms
from . import models
from django.forms import ModelForm

#L
class GenreModelForm(forms.ModelForm):
    class Meta: 
        model = models.Genre
        fields = [
           "name", "description"]

class AuthorModelForm(forms.ModelForm):
    class Meta: 
        model = models.Author
        fields = [
           "name", "description"]
        
class SeriesModelForm(forms.ModelForm):
    class Meta: 
        model = models.Series
        fields = [
           "name"]
        
class PublishModelForm(forms.ModelForm):
    class Meta: 
        model = models.Publish
        fields = [
           "name", "description"]
        
class StatusModelForm(forms.ModelForm):
    class Meta: 
        model = models.Publish
        fields = [
           "name", "description"]