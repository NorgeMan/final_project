from django.urls import path
from .views import UserSignUpView, UserEditView, ChangePasswordsView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign-up/', UserSignUpView.as_view(), name='sign-up'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', ChangePasswordsView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name="password_success"),
]
