from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


# app_name = 'userside'

urlpatterns = [
    path('', views.home, name='home_user'),
    path('register_user/', views.register, name='register_user'),
    path('profile_user/', views.profile, name='profile_user'),
    path('login_user/', auth_view.LoginView.as_view(template_name='Authentication/login.html'), name="login_user"),
    path('logout_user/', auth_view.LogoutView.as_view(template_name='Authentication/logout.html'), name="logout_user"),
]