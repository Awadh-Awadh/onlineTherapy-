from .models import CustomUser, Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model



@receiver(post_save,sender = get_user_model)
def create_user_profile(instance, created, sender, **kwargs):
  if created:
    Profile.objects.create(user = instance)
