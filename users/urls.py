from django.urls import path
from .views import UserSignUpView, UserEditView

urlpatterns = [
    path('sign-up/', UserSignUpView.as_view(), name='sign-up'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
]
