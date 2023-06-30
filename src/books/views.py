from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . import forms
from reference.models import Author, Genre, Series, Publish

# Create your views here.

class BooksListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url=reverse_lazy('person:login')
    permission_required=['reference.add_genre','reference.delete_genre', 'books.add_book', 'books.delete_book', 'books.change_book' ]
    model = models.Book
    

#Read 
class BookView(generic.DetailView):
    model = models.Book
    template_name= 'books/book_detail.html' 

#Create
class BooksCreateView(generic.CreateView):
    model = models.Book
    form_class = forms.BooksModelForm
       
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()

#Update   
class BooksUpdateView(generic.UpdateView):
    model= models.Book
    form_class= forms.BooksModelForm
    
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()

# Delete  
class BooksDeleteView(generic.DeleteView):
    model= models.Book
    template_name = 'books/book_delete.html' 
    success_url = '/books/books-list'

