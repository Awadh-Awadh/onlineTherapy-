from typing_extensions import ParamSpecKwargs
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomManager(BaseUserManager):


    def create_user(self, email, username, firstname, lastname, password, **other_fields):
      if not email:
        raise ValueError(_("value must be set"))

      email = self.normalize_email(email)
      user = self.models(username = username, email=email, firstname=firstname,
                         lastname=lastname, **other_fields)
      user.set_password(password)
      return user

    def create_superuser(self, email, username, firstname, lastname, password, **otherfiels):
        otherfiels.setdefault("is_staff", True)
        otherfiels.setdefault("is_superuser", True)
        otherfiels.setdefault("is_active", True)

        if otherfiels.get('is_staff') is not True:
          raise ValueError("Supper user must have the value is_staff = True")
        if otherfiels.get('is_supperuser') is not True:
          raise ValueError("Supper user must have the value is_superuser = True")

        return self.create_user(email=email, username=username, firstname=firstname,
                                lastname=lastname, password=password, **otherfiels
                                )         