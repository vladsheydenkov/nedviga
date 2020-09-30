from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Apartments(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255,
                            unique_for_date='publish')

    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='user_apartments')