from django.db import models
from django.urls import reverse_lazy
from PIL import Image
from pathlib import Path
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    name = models.CharField(
        verbose_name='Book name',
        max_length=30)
    picture = models.ImageField(
        verbose_name='picture book', 
        upload_to='uploads/genre/', 
        default='uploads/genre/image.png', 
        blank=True)
    price = models.DecimalField(
        verbose_name='Price',
        default=0,
        max_digits=6,
        decimal_places=2)
    author = models.ManyToManyField(
        "reference.Author",
        verbose_name='Author',
        related_name='books_author')
    series = models.ForeignKey(
        "reference.Series",
        on_delete=models.PROTECT,
        verbose_name='Series',
        related_name='books_series')
    genre = models.ForeignKey(
        "reference.Genre",
        on_delete=models.PROTECT,
        verbose_name='Genre',
        related_name='books_genre')
    year = models.BigIntegerField(
        verbose_name='Year book',
        blank=True,
        null=True)
    pages = models.BigIntegerField(
        verbose_name='Number of pages',
        blank=True,
        null=True)
    pereplet = models.CharField(
        verbose_name='Pereplet book',
        max_length=20,
        blank=True,
        default="hardcover")
    formatbook = models.CharField(
        verbose_name='format book',
        max_length=30,
        blank=True,
        default="encyclopedi")
    isbn = models.BigIntegerField(
        verbose_name='ISBN book',
        blank=True,
        null=True)
    ves = models.BigIntegerField(
        verbose_name='ves book',
        blank=True,
        null=True)
    agerestrict = models.CharField(
        verbose_name='Age restrictions book',
        max_length=4,
        blank=True,
        default="6+")
    publish = models.ForeignKey(
        "reference.Publish",
        on_delete=models.PROTECT,
        verbose_name='Publish',
        related_name='books_publish')
    quantity = models.BigIntegerField(
        verbose_name='Number of books',
        blank=True,
        default=1)
    activ = models.BooleanField(
        default=True)
    rating = models.BigIntegerField(
        verbose_name='rating books',
        blank=True,
        default=1)
    dateadd = models.DateTimeField(
        verbose_name='Date add',
        auto_now=False,
        auto_now_add=True,
        blank=True)
        # default=timezone.now
    dateupdate = models.DateTimeField(
        verbose_name='Date update',
        auto_now=True,
        auto_now_add=False,
        blank=True)
       
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('books:BooksListView')
        # reverse_lazy('reference:GenreView', kwargs={"pk":self.pk})
        # return f"/genre/{self.pk}"

    def genre_picture_med(self):
        original_url = self.picture.url
        new_url = original_url.split('.')
        picture_url = '.'.join(new_url[:-1])+'_140_.' + new_url[-1]
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
        for m_basewidth in [140,40]:
            im = Image.open(self.picture.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(str(BASE_DIR/"".join(file_name[:-1]))+f'_{m_basewidth}_.'+extention)