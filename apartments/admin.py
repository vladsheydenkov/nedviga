from django.contrib import admin
from .models import Apartments


@admin.register(Apartments) 
class ApartmentsAdmin(admin.ModelAdmin):
    list_filter = ('quality', 'auction', 'rooms', 'created')
    list_display = (Apartments.__str__, 'created', 'updated')
    readonly_fields = ('created', 'updated')

   
# Register your models here.