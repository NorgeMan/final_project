from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .forms import SignUpForm, EditProfileForm, PasswordChangesForm
from the_diary.models import Profile


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


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context
