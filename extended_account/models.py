from django.db import models
from django.contrib.auth.models import User


class Appearance(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_url = models.URLField(default="img/book2.jpg")
