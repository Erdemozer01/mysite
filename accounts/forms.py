from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from posts.models.posts import Posts
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    terms = forms.BooleanField(required=True, label="Kullanıcı Şartlarını kabul ediyorum.")


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı Adı'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyadınız'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['cover', 'avatar', 'about', 'phone', 'job', 'location', 'facebook', 'twitter', 'instagram']
        widgets = {
            'birth_day': forms.DateInput(attrs={'class': "form-control datepicker"}),
        }
