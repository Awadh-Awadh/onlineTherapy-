from django.contrib.auth import get_user_model
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser, Conditions
from datetimepicker.widgets import DateTimePicker



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




from datetimepicker.widgets import DateTimePicker


class SampleForm(forms.Form):
  datetime = forms.DateTimeField(
  widget=DateTimePicker(),
  )

