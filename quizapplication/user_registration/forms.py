from django import forms
from django.contrib.auth.models import User
from .models import UserInfo



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class UserInfoForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False)
    class Meta():
        model = UserInfo
        fields = ('address', 'phone', 'profile_image')
        

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')