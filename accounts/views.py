from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.views import generic


class Login(LoginView):
    template_name = 'registration/login.html'


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
                          'blog/home.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'accounts/register.html',
                  {'user_form': user_form, 'msg': user_form.errors})


class ProfileView(generic.ListView):
    template_name = 'profile/home.html'
    queryset = Profile.objects.all()
    context_object_name = 'profile'


class ProfileEdit(generic.UpdateView):
    template_name = 'profile/pages/edit.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile:home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Profil Güncellendi")
        return super(ProfileEdit, self).form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user
