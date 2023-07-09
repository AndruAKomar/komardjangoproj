from django import forms
from . import models
from django.forms import ModelForm


class CreateOrderForm(forms.Form):
    delivery_adress = forms.CharField(
        required=True,
        widget =forms.Textarea
    )

class OrderModelForm(forms.ModelForm):
    class Meta: 
        model = models.Order
        fields = ['status', 'delivery_adress']

class OrderDetailForm(forms.ModelForm):
    class Meta: 
        model = models.Order
        fields = ('status', 'delivery_adress', 'cart')