#from django.shortcuts import render
from django.views import generic

# Create your views here.

#HomePage 
class HomePage(generic.TemplateView):
    template_name='home/index.html'