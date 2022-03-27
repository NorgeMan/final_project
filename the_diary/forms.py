from django import forms
from .models import Publication, Category


choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'category', 'author', 'start_time', 'end_time', 'summary', 'publication_date')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'readonly': 'True'}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'category', 'start_time', 'end_time', 'summary')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'start_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
        }
