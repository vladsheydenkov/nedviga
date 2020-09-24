from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.



def r(request):
    return render(request,'index.html')