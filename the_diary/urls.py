from django.urls import path
from . import views
from .views import Home, PublicationDetailedView, AddPublicationView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('publication/<int:pk>', PublicationDetailedView.as_view(), name="publication-detail"),
    path('add/', AddPublicationView.as_view(), name='add'),
]
