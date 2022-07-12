from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from posts.models.posts import Posts
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth.views import LoginView


class Login(LoginView):
    template_name = 'accounts/../templates/registration/login.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])

            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(
                user=new_user,
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
                email=user_form.cleaned_data['email'],
            )

            login(request, new_user)
            return render(request,
                          'profile/home.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form})
