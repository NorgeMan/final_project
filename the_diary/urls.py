from django.urls import path
from . import views
from .views import Home, PublicationDetailedView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('publication/<int:pk>', PublicationDetailedView.as_view(), name="publication-detail"),
]
