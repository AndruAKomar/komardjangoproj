from django.urls import path
from . import views

app_name='person'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    
]
