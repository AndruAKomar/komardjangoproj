from django import forms
from . import models
from django.forms import ModelForm

#L
class BooksModelForm(forms.ModelForm):
    class Meta: 
        model = models.Book
        fields = [
            "name",
            "picture",
            "price",
            "author",
            "genre",
            "series",
            "year", 
            "pages",
            "pereplet",
            "formatbook", 
            "isbn", 
            "ves",
            "agerestrict",
            "publish",
            "quantity",
            "activ",
            "rating",
            
            ]








