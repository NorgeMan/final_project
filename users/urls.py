from django.urls import path
from .views import UserSignUpView

urlpatterns = [
    path('sign-up/', UserSignUpView.as_view(), name='sign-up'),

]
