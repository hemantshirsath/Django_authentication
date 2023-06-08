from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class Registeration(UserCreationForm):
    password2=forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class normaluser(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class adminuser(UserChangeForm):
    class Meta:
        model=User
        fields="__all__"
