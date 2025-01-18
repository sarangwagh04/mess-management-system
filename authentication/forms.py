# authentication/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['is_hostel_member', 'is_mess_member']  # Add additional fields as needed
