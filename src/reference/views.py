from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from django.views import generic
from . import models
from . import forms
from .models import Author, Genre, Series, Publish

# Create your views here.

# def home_page(request):
#     return HttpResponse('reference')

#test Read:
# def view_refer_genre(request, pk):
#     genr = models.Genre.objects.get(pk=int(pk))
#     html = f"Genre - {genr.pk} : {genr.name}"
#     return HttpResponse(html)  

# test 2 
# def home_page(request):
#     return render(request, template_name='reference/index.html', context={'key': models.Genre.objects.get(pk=1)})

# #success
# def success_page(request):
#     return render (request, template_name='reference/success.html', context={'key': models.Genre.objects.get(pk=1)})

#_____________________________________________________________________#

#Read 
class GenreView(generic.DetailView):
    model = models.Genre

class AuthorView(generic.DetailView):
    model = models.Author
    

#List 
class GenreListView(generic.ListView):
    model = models.Genre
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        cont["author_list"] = Author.objects.all()
        cont["series_list"] = Series.objects.all()
        cont["publish_list"] = Publish.objects.all()
        return cont


#Create
class GenreCreateView(generic.CreateView):
    model = models.Genre
    #template_name = 'reference/genre_form.html'
    fields = [
        "picture", "name", "description"
    ]
    def get_success_url(self) -> str:
        return super().get_success_url()

#Updata
class GenreUpdateView(generic.UpdateView):
    model = models.Genre
    template_name = 'reference/genre_update.html'
    form_class= forms.GenreModelForm
    
#Delete
class GenreDeleteView(generic.DeleteView):
    model = models.Genre
    template_name = 'reference/genre_delete.html' 
    success_url = '/'
