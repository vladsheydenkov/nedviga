from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from apartments import views
from . import views

app_name = 'user'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')

]