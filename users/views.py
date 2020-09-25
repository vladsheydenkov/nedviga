from django.shortcuts import render
from . import forms
from .models import ProfileUser


def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            ProfileUser.objects.create(user=new_user)
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = forms.UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})