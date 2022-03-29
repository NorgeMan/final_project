from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangesForm


class UserSignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ChangePasswordsView(PasswordChangeView):
    form_class = PasswordChangesForm
    # form_class = PasswordChangeForm
    # success_url = reverse_lazy('home')
    success_url = reverse_lazy('password_success')
