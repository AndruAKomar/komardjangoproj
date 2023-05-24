from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from . import models

# Create your views here.
def home_page(request):
    return HttpResponse('reference')

#test Read:
def view_refer_genre(request, pk):
    genr = models.Genre.objects.get(pk=int(pk))
    html = f"Genre - {genr.pk} : {genr.name}"
    return HttpResponse(html)  