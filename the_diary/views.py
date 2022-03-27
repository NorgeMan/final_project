from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publication, Category
from .forms import PublicationForm, EditForm
from django.urls import reverse_lazy


class Home(ListView):
    model = Publication
    template_name = 'home.html'
    ordering = ['-publication_date', '-id']

    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class PublicationDetailedView(DetailView):
    model = Publication
    template_name = 'details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PublicationDetailedView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


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


def category_list_view(request):
    category_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'category_menu_list': category_menu_list})
