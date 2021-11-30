from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password, **other_fields):
      if not email:
        raise ValueError(_("value must be set"))

      email = self.normalize_email(email)
      user = self.model(username = username, email=email, firstname=firstname,
                         lastname=lastname, **other_fields)
      user.set_password(password)
      user.save()
      return user


    def create_superuser(self, email, username, firstname, lastname, password,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email,username, firstname, lastname, password,**extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):

  email = models.EmailField(_("Email Field"), unique=True)
  username = models.CharField(max_length=255, unique=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=200)
  start_date = models.DateTimeField(default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username','firstname','lastname']
  
   
  def __str__(self):
    return self.username


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    about = models.TextField(max_length=300)
     
    def __str__(self):
      return self.user.username


class Conditions(models.Model):
  condition = models.TextField()
  name = models.CharField(max_length=255)
  def __str__(self):
      return self.name