from django.contrib import admin
from django.urls import path
from apartments import views

app_name = 'apartments'


urlpatterns = [
    # path('', views.r),
    path('', views.all_apartments,
         name='all_apartments'),

]
