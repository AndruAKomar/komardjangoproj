from django.db import models
from django.urls import reverse_lazy
from PIL import Image
from pathlib import Path
    
# Create your models here.

class Genre(models.Model):
    name = models.CharField(verbose_name='Genre name', max_length=50)
    description = models.TextField(verbose_name='Genre description', null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('reference:ReferenceListView')
        
    
class Author(models.Model):
    name = models.CharField(verbose_name='Author name', max_length=30)
    description = models.TextField(verbose_name='Author description', null=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse_lazy('reference:AuthorView', kwargs={"pk":self.pk})

    
class Series(models.Model):
    name = models.CharField(verbose_name='Series book', max_length=50)
    def __str__(self) -> str:
        return str(self.name)
       

class Publish(models.Model):
    name = models.CharField(verbose_name='Publishing office', max_length=50)
    description = models.TextField(verbose_name='Publishing office description', null=True, blank=True)
    def __str__(self):
        return self.name

    
class Status(models.Model):
    name = models.CharField(verbose_name='Order_status', max_length=20)
    def __str__(self):
        return self.name

    

