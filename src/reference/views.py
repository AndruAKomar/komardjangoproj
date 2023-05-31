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
def view_refer_genre(request, pk):
    genr = models.Genre.objects.get(pk=int(pk))
    html = f"Genre - {genr.pk} : {genr.name}"
    return HttpResponse(html)  

# test 2 
def home_page(request):
    return render(request, template_name='reference/index.html', context={'key': models.Genre.objects.get(pk=1)})

# #success
# def success_page(request):
#     return render (request, template_name='reference/success.html', context={'key': models.Genre.objects.get(pk=1)})

#List 
class HomePage(generic.TemplateView):
    template_name='reference/index.html'

#Read 
class GenreView(generic.DetailView):
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
    #template_name = 'reference/genre_form.html'
    form_class= forms.GenreModelForm
    

