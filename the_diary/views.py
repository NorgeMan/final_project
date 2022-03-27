from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Publication, Category
from .forms import PublicationForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


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

        stuff = get_object_or_404(Publication, id=self.kwargs['pk'])
        count_likes = stuff.count_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["count_likes"] = count_likes
        context["liked"] = liked
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


def like_view(request, pk):
    publication = get_object_or_404(Publication, id=request.POST.get('publication_id'))
    liked = False
    if publication.likes.filter(id=request.user.id).exists():
        publication.likes.remove(request.user)
        liked = False
    else:
        publication.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('publication-detail', args=[str(pk)]))

