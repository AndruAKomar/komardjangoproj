from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib.auth.models import Group

# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = 'person/login.html'

class LogoutView(auth_views.LogoutView):
    template_name = 'person/logout.html'

# create customer


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
            return render(request, 'person/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'person/register.html', {'user_form': user_form})