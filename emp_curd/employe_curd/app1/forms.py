from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class emp(forms.ModelForm):
    class Meta:
        model=Management_Employee
        fields=['name','email','pwd','emp_id']
        labels={'name':'Enter Name','email':'Enter Email','pwd':'Enter Password'}

class signupform(UserCreationForm):
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']


