from django.contrib import admin
from django.urls import path
from apartments import views

app_name = 'apartments'


urlpatterns = [
    path('', views.index),
    path('search', views.search_appartments, name='search_result'),

]
