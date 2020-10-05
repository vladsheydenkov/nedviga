from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
# from django.contrib.auth.models import User
# Create your models here.

class Apartments(models.Model):

    QUALITY_CHOICES = [('0','new'),
                        ('1','used')]
    AUCTION_CHOICES = [('0','no'),
                        ('1','yes')] 

    quality = models.CharField(choices=QUALITY_CHOICES, default='not a mention', max_length=225)
    auction = models.CharField(choices=AUCTION_CHOICES, default='0', max_length=225)
    area_sq = models.PositiveSmallIntegerField(default=1, blank=False, null=False)
    price = models.DecimalField(decimal_places=2,max_digits=12, blank=False, null=False) # $$$
    rooms = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(10)], blank=False, null=False)
    address = models.CharField(max_length=225,blank=False)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 
    # author = models.ForeignKey(User,
    #                            on_delete=models.CASCADE,
    #                            related_name='user_apartments')
    
    #contacts = User.contacts

    class Meta:
        verbose_name_plural = 'Apartments'

    def __str__(self):
        return  'Квартира на ' + self.address





