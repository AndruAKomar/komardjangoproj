from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Genre)
admin.site.register(models.Authors)
admin.site.register(models.Publish)
admin.site.register(models.Series)