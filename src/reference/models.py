from django.db import models

# Create your models here.

class Genres(models.Model):
    name = models.CharField(verbose_name='Genre name', max_length=50)
    description = models.TextField(verbose_name='Genre description', null=True, blank=True)

    def __str__(self):
        return self.name
