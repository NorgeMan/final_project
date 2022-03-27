from django.urls import path
from . import views
from .views import Home, PublicationDetailedView, AddPublicationView, UpdatePublicationView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('publication/<int:pk>', PublicationDetailedView.as_view(), name="publication-detail"),
    path('add/', AddPublicationView.as_view(), name='add'),
    path('publication/edit/<int:pk>', UpdatePublicationView.as_view(), name="publication-update"),
]
