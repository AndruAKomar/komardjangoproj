from django import forms
from . import models
from orders.models import Order
from .models import Person
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserDetailForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ('username', 'first_name','last_name', 'email')

# рассширяем модель ЮЗЕР доп полями ПЕРСОН. Создаем вторую форму
 
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')

class PersonUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('telephone_number', 'home_address', 'delivery_adress')

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    telephone_number = forms.CharField(label='Telephone_number', widget=forms.TextInput, max_length=50, required=False, initial="undefined")
    home_address = forms.CharField(label='Home_address', widget=forms.TextInput, max_length=50, required=False, initial="undefined")
    delivery_adress = forms.CharField(label='Delivery_adress', widget=forms.TextInput, max_length=50, required=False, initial="undefined")
    
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    
class PersonRegistrationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('telephone_number', 'home_address','delivery_adress')
