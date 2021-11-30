from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomManager
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(_("Email Field"), unique=True)
  username = models.CharField(max_length=255, unique=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=200)
  start_date = models.DateTimeField(default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  objects = CustomManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ('email', 'username')
  
   
  def __str__(self):
    return self.username



class Profile:
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pp = ...
    about = models.TextField(max_length=300)