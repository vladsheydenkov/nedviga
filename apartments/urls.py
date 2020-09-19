from django.contrib import admin
from django.urls import path
from apartments import views

app_name = 'apartmens'


urlpatterns = [
    path('', views.r),

]
