from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('publication-detail', args=(str(self.id)))
        return reverse('home')


class Publication(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default="training")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now, blank=False)
    end_time = models.DateTimeField(default=datetime.now, blank=False)
    summary = models.TextField()
    publication_date = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('publication-detail', args=(str(self.id)))
        return reverse('home')
