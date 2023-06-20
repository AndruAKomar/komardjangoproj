from django.db import models
from django.urls import reverse_lazy
from PIL import Image
from pathlib import Path
    
# Create your models here.

class Genre(models.Model):
    name = models.CharField(verbose_name='Genre name', max_length=50)
    description = models.TextField(verbose_name='Genre description', null=True, blank=True)
    picture = models.ImageField(verbose_name='picture name', upload_to='uploads/genre/', default='uploads/genre/real-friends.jpg', blank=True)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('reference:ReferenceListView')
        # reverse_lazy('reference:GenreView', kwargs={"pk":self.pk})
        # return f"/genre/{self.pk}"

    def genre_picture_med(self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = '.'.join(new_url[:-1])+'_150_.' + new_url[-1]
        return picture_url
    
    def genre_picture_small(self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = '.'.join(new_url[:-1])+'_40_.' + new_url[-1]
        return picture_url
    
    def picture_resizer(self):
        extention =self.picture.file.name.split('.')[-1]
        BASE_DIR = Path(self.picture.file.name).resolve().parent
        file_name = Path(self.picture.file.name).resolve().name.split('.')
        for m_basewidth in [150,40]:
            im = Image.open(self.picture.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(str(BASE_DIR/"".join(file_name[:-1]))+f'_{m_basewidth}_.'+extention)
    

class Author(models.Model):
    name = models.CharField(verbose_name='Author name', max_length=30)
    description = models.TextField(verbose_name='Author description', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('reference:AuthorView', kwargs={"pk":self.pk})
    
class Series(models.Model):
    name = models.CharField(verbose_name='Series book', max_length=50)
    # name = models.BigIntegerField(verbose_name='Series book')
    
    def __str__(self) -> str:
        return str(self.name)
    
class Publish(models.Model):
    name = models.CharField(verbose_name='Publishing office', max_length=50)
    description = models.TextField(verbose_name='Publishing office description', null=True, blank=True)

    def __str__(self):
        return self.name