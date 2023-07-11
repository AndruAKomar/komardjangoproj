from typing import Any, Dict
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from . import forms
from .models import Person
from orders.models import Order, Cart
from orders.forms import OrderModelForm, OrderDetailForm
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import UserRegistrationForm, PersonRegistrationForm, UserUpdateForm, PersonUpdateForm, UserDetailForm
from django.urls import reverse_lazy

# 
class LoginView(auth_views.LoginView):
    template_name = 'person/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'person/logout.html'


#users List
class UsersListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    login_url=reverse_lazy('person:login')
    permission_required=['reference.add_genre','reference.delete_genre', 'books.add_book', 'books.delete_book', 'books.change_book' ]
    model = User
    template_name = 'person/user_list.html'

    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont["order_list"] = Order.objects.all()
        cont["person_list"] = Person.objects.all()
        
        # cont["total_quantity_in_cart"] = Order.objects.get(pk=3)
        # cont["total"] = Order.objects.get(pk=7).cart.customer
        # cont["total"] = Order.objects.all()
        return cont

# 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='Customers'))
            # Create the user person with доп параметры
            telephone_number = user_form.cleaned_data.get('telephone_number')
            home_address = user_form.cleaned_data.get('home_address')
            delivery_adress = user_form.cleaned_data.get('delivery_adress')
            person = Person.objects.create(
                user=new_user, 
                telephone_number = telephone_number,
                home_address = home_address, 
                delivery_adress = delivery_adress)
            return render(request, 'person/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'person/register.html', {'user_form': user_form})



# @login_required
def update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(instance=request.user, data=request.POST)
        person_form = PersonUpdateForm(instance=request.user.person, data=request.POST, files=request.FILES)
        if user_form.is_valid() and person_form.is_valid():
            user_form.save()
            person_form.save()
            return render(request, 'person/register_done.html')
    else:
        user_form = UserUpdateForm(instance=request.user)
        person_form = PersonUpdateForm(instance=request.user.person)
        return render(request,
                      'person/user_update.html',
                      {'user_form': user_form,
                       'person_form': person_form})
    

#Detail    
class UserDetailView(generic.DetailView):
    model= User
    template_name = 'person/user_detail.html'
    success_url = '/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont =super().get_context_data(**kwargs)        
        cont["object_order"] = Order.objects.all()
        return cont