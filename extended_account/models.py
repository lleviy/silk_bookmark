from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Appearance(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_url = models.URLField(default="https://images.unsplash.com/photo-1512580770426-cbed71c40e94?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1982&q=80")

    @receiver(post_save, sender=User)
    def create_user_appearance(sender, instance, created, **kwargs):
        if created:
            Appearance.objects.create(owner=instance)
