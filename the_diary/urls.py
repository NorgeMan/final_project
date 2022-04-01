from django.urls import path
from . import views
from .views import Home, PublicationDetailedView, AddPublicationView, UpdatePublicationView, DeletePublicationView, AddCommentView
from .views import AddCategoryView, category_view, category_list_view, like_view

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('publication/<int:pk>', PublicationDetailedView.as_view(), name="publication-detail"),
    path('add/', AddPublicationView.as_view(), name="add"),
    path('publication/edit/<int:pk>', UpdatePublicationView.as_view(), name="publication-update"),
    path('publication/<int:pk>/delete', DeletePublicationView.as_view(), name="publication-delete"),
    path('add-category/', AddCategoryView.as_view(), name="add-category"),
    path('category/<str:categories>/', category_view, name="category"),
    path('category-list/', category_list_view, name="category-list"),
    path('like/<int:pk>', like_view, name='like_publication'),
    path('publication/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
]
