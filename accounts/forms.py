from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser, Conditions, Profile



class CustomCreationForm(UserCreationForm):
   class Meta:
     model = CustomUser
     fields = ['username','firstname', 'lastname', 'email']

class CustomChangeForm(UserChangeForm):
  class Meta:
    model = CustomUser
    fields = ['email', 'username', 'firstname', 'lastname']


class ConditionForm(forms.ModelForm):
    class Meta:
       model = Conditions
       fields = '__all__'
       exclude = ['user']

class ProfileUpdate(forms.ModelForm):
  username = forms.CharField(max_length=255)
  class Meta:
    model = Profile
    fields = ['bio']
    
