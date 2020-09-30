from django import forms
from .models import Apartments


class Ad_form(forms.ModelForm):

    class Meta:
        models = Apartments
        # fields = ('quality',"area_sq",'price','rooms','address')
        fields= '__all__'