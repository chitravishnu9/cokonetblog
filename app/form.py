from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import blog


class blogForm(forms.ModelForm):
    class Meta:
        model=blog
        fields='__all__'


class RegistrationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['first_name','last_name','email','username','password1','password2']
