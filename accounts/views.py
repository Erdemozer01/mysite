from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile
from django.contrib.auth.views import LoginView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginView):
    template_name = 'registration/login.html'


class RegisterView(generic.CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request, 'Başarılı Bir Şekilde Kayıt Oldunuz.')
        form.save()
        return super(RegisterView, self).form_valid(form)


class ProfileView(generic.ListView):
    model = Profile
    template_name = 'profile/home.html'
    queryset = Profile.objects.all()
    context_object_name = 'profile'

    def get_queryset(self):
        return self.model.user


class BasicProfileUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name = 'profile/edit/basic.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile:basic')
    model = User

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def profile_detail(request, pk, user):
    profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    user_form = UserUpdateForm(request.POST)
    if request.method == "POST":
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('blog:home')
        else:
            form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    return render(request, 'profile/edit/detail.html', {'profile_form': profile_form, 'user_form': user_form})
