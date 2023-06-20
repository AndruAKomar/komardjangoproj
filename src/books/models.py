from django.db import models
from django.urls import reverse_lazy
from PIL import Image
from pathlib import Path

# Create your models here.

class Book(models.Model):
    name = models.CharField(
        verbose_name='Book name',
        max_length=30)
    picture = models.ImageField(
        verbose_name='picture book', 
        upload_to='uploads/genre/', 
        default='uploads/genre/real-friends.jpg', 
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
        verbose_name='Year book')
    
    
    def __str__(self):
        return self.name