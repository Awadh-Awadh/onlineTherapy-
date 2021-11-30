from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


class CustomCreationForm(UserCreationForm):
   class Meta:
     model = get_user_model()

     field = ('email', 'username',)

class CustomChangeForm(UserChangeForm):
  class Meta:
    model = get_user_model
    field = ('email', 'username', 'firstname', 'lastname')