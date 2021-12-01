from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomCreationForm(UserCreationForm):
   class Meta:
     model = CustomUser
     fields = ['username','firstname', 'lastname', 'email']

class CustomChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ['email', 'username', 'firstname', 'lastname']