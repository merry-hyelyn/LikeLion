from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispathch import receiver

# Create your models here.


class Profile(model.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(nell=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Login.objects.create(user=instance)
