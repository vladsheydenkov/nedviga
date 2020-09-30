from django.shortcuts import render
from .models import Apartments
from . import forms



def index(request):

    return render(request,'index.html')


def search_appartments(request):

    quality, rooms,price = request.POST['quality'], request.POST['rooms'], request.POST['price']

    try: #  ignore blank/wrong price
        int(price)
        search_by_parametrs = Apartments.objects.filter(quality=quality).filter(rooms=rooms).filter(price__lte=price).all()
    except ValueError:
        search_by_parametrs = Apartments.objects.filter(quality=quality).filter(rooms=rooms).all()

    return  render (request, 'search_result.html', {'search_by_parametrs':search_by_parametrs})

    
# def create_ad(request): # для добавления объявлений с сайта
#         ad_form = forms.Ad_form(request.POST)
#         if ad_form.is_valid():
#         new_ad = ad_form.save()
#                 apartments = Apartments.objects.create(*)
