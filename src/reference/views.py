from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from . import models
from . import forms
from .models import Author, Genre, Series, Publish
from django.urls import reverse_lazy

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

#__________________________________________________________________#


#Read 
class GenreView(generic.DetailView):
    model = models.Genre
    template_name = 'reference/reference_detail.html'
    
class AuthorView(generic.DetailView):
    model = models.Author
    template_name = 'reference/reference_detail.html'

class SeriesView(generic.DetailView):
    model = models.Series
    template_name = 'reference/reference_detail.html'

class PublishView(generic.DetailView):
    model = models.Publish
    template_name = 'reference/reference_detail.html'   

#List 
class ReferenceListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url=reverse_lazy('person:login')
    permission_required=['reference.add_genre','reference.delete_genre']
    model = models.Genre
    template_name = 'reference/reference_list.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)
        cont["author_list"] = Author.objects.all()
        cont["series_list"] = Series.objects.all()
        cont["publish_list"] = Publish.objects.all()
        return cont


#Create
class GenreCreateView(generic.CreateView):
    model = models.Genre
    template_name = 'reference/reference_form.html'
    fields = [
        "picture", "name", "description"
    ]
    
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()

class AuthorCreateView(generic.CreateView):
    model = models.Author
    template_name = 'reference/reference_form.html'
    fields = [
        "name", "description"
    ]
    success_url = '/reference/reference-list'

    def get_success_url(self) -> str:
        return super().get_success_url()

class SeriesCreateView(generic.CreateView):
    model = models.Series
    template_name = 'reference/reference_form.html'
    fields = [
        "name"
    ]
    success_url = '/reference/reference-list'
    
    def get_success_url(self) -> str:
        return super().get_success_url()

class PublishCreateView(generic.CreateView):
    model = models.Publish
    template_name = 'reference/reference_form.html'
    fields = [
        "name", "description"
    ]
    success_url = '/reference/reference-list'

    def get_success_url(self) -> str:
        return super().get_success_url()

#Updata
class GenreUpdateView(generic.UpdateView):
    model = models.Genre
    template_name = 'reference/reference_update.html'
    form_class= forms.GenreModelForm

    # def form_valid(self, form):
    #     # if form.has_changed():
    #     #     if 'picture' in form.changed_data:
    #     self.object.picture_resizer()
    #     return super().form_valid(form)
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
 
class AuthorUpdateView(generic.UpdateView):
    model = models.Author
    template_name = 'reference/reference_update.html'
    form_class= forms.AuthorModelForm
    success_url = '/reference/reference-list' 

class SeriesUpdateView(generic.UpdateView):
    model = models.Series
    template_name = 'reference/reference_update.html'
    form_class= forms.SeriesModelForm
    success_url = '/reference/reference-list'   

class PublishUpdateView(generic.UpdateView):
    model = models.Publish
    template_name = 'reference/reference_update.html'
    form_class= forms.PublishModelForm
    success_url = '/reference/reference-list'  

#Delete
class GenreDeleteView(generic.DeleteView):
    model = models.Genre
    template_name = 'reference/reference_delete.html' 
    success_url = '/reference/reference-list'

class AuthorDeleteView(generic.DeleteView):
    model = models.Author
    template_name = 'reference/reference_delete.html' 
    success_url = '/reference/reference-list'

class SeriesDeleteView(generic.DeleteView):
    model = models.Series
    template_name = 'reference/reference_delete.html' 
    success_url = '/reference/reference-list'

class PublishDeleteView(generic.DeleteView):
    model = models.Publish
    template_name = 'reference/reference_delete.html' 
    success_url = '/reference/reference-list'
    
