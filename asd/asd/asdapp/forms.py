
from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
# from asdapp.models import UserProfileInfo

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    dob = forms.DateField()
    class Meta:
        model =User
        fields = ('username','email','password','dob')