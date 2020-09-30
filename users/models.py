from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)
    first_name = models.CharField(max_length=90, blank=True)
    last_name = models.CharField(max_length=90, blank=True)



