# forms.py
from django import forms
from .models import UserActivityRegistration

class RegistrationForm(forms.ModelForm):
    name_user = forms.CharField(max_length=15, label='Name User')

    phone_number = forms.CharField(max_length=15, label='Phone Number')

    class Meta:
        model = UserActivityRegistration
        fields = ['name_user']
        fields = ['phone_number']

# class InitialRegistrationForm(forms.ModelForm):
#     name_user = forms.CharField(max_length=15, label='Name User')

#     phone_number = forms.CharField(max_length=15, label='Phone Number')

#     class Meta:
#         model = UserActivityRegistration
#         fields = ['name_user']
#         fields = ['phone_number']
   
