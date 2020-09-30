from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Apartments)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
