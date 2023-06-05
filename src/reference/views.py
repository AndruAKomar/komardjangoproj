from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from django.views import generic
from . import models
from . import forms

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

#List 
class GenreListView(generic.ListView):
    model = models.Genre


#Create
class GenreCreateView(generic.CreateView):
    model = models.Genre
    #template_name = 'reference/genre_form.html'
    fields = [
        "name", "description"
    ]

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
