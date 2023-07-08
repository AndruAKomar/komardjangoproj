from django.urls import path
from . import views

app_name='person'
urlpatterns = [
    path('user-list/', views.UsersListView.as_view(), name='UsersListView'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user-update/<int:pk>', views.UserUpdateView.as_view(), name='user-update'),
    path('user-detail/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('register/', views.register, name='register'),
    
    
]
