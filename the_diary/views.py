from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publication


# def home(request):
#    return render(request, 'home.html', {})

class Home(ListView):
    model = Publication
    template_name = 'home.html'


class PublicationDetailedView(DetailView):
    model = Publication
    template_name = 'details.html'