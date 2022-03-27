from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publication
from .forms import PublicationForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#    return render(request, 'home.html', {})


class Home(ListView):
    model = Publication
    template_name = 'home.html'
    ordering = ['-id']


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
