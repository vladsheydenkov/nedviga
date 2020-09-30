from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from . import models


def r(request):
    return render(request,'index.html')


def all_apartments(request):
    apartments = models.Apartments.objects.all()
    return render(request,
                  'apartments/apartments.html',
                  {'apartments': apartments})
