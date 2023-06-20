from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from . import models
from reference.models import Author, Genre, Series, Publish

# Create your views here.

class BooksListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url=reverse_lazy('person:login')
    #permission_required=['reference.add_genre','reference.delete_genre']
    model = models.Book