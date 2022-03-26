from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Publication
from .forms import PublicationForm

# def home(request):
#    return render(request, 'home.html', {})


class Home(ListView):
    model = Publication
    template_name = 'home.html'


class PublicationDetailedView(DetailView):
    model = Publication
    template_name = 'details.html'


class AddPublicationView(CreateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'add.html'
