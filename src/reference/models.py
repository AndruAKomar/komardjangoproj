from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Genre(models.Model):
    name = models.CharField(verbose_name='Genre name', max_length=50)
    description = models.TextField(verbose_name='Genre description', null=True, blank=True)
    picture = models.ImageField(verbose_name='picture name', upload_to='uploads/genre/')
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('reference:GenreView', kwargs={"pk":self.pk})
        # return f"/genre/{self.pk}"

class Author(models.Model):
    name = models.CharField(verbose_name='Author name', max_length=30)
    description = models.TextField(verbose_name='Author description', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('reference:AuthorView', kwargs={"pk":self.pk})
    
class Series(models.Model):
    name = models.BigIntegerField(verbose_name='Series book')
    
    def __str__(self) -> str:
        return str(self.name)
    
class Publish(models.Model):
    name = models.CharField(verbose_name='Publishing office', max_length=50)
    description = models.TextField(verbose_name='Publishing office description', null=True, blank=True)

    def __str__(self):
        return self.name