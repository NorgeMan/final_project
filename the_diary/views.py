from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publication, Category
from .forms import PublicationForm, EditForm
from django.urls import reverse_lazy


# def home(request):
#    return render(request, 'home.html', {})


class Home(ListView):
    model = Publication
    template_name = 'home.html'
    ordering = ['-publication_date', '-id']
    # ordering = ['-id']


class PublicationDetailedView(DetailView):
    model = Publication
    template_name = 'details.html'


class AddPublicationView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'add.html'


class UpdatePublicationView(UpdateView):
    model = Publication
    form_class = EditForm
    template_name = 'update.html'


class DeletePublicationView(DeleteView):
    model = Publication
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


def category_view(request, categories):
    category_publications = Publication.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'categories.html',
                  {'categories': categories.title().replace('-', ' '), 'category_publications': category_publications})
