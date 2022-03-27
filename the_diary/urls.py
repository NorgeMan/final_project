from django.urls import path
from . import views
from .views import Home, PublicationDetailedView, AddPublicationView, UpdatePublicationView, DeletePublicationView
from .views import AddCategoryView, category_view

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('publication/<int:pk>', PublicationDetailedView.as_view(), name="publication-detail"),
    path('add/', AddPublicationView.as_view(), name="add"),
    path('publication/edit/<int:pk>', UpdatePublicationView.as_view(), name="publication-update"),
    path('publication/<int:pk>/delete', DeletePublicationView.as_view(), name="publication-delete"),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:categories>/', category_view, name="category"),
]
