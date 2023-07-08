from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'telephone_number',
        'home_address',
        'delivery_adress']

admin.site.register(Person, PersonAdmin)
