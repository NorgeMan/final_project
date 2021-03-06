from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField


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
    # summary = models.TextField()
    summary = RichTextField(blank=True, null=True)
    publication_date = models.DateField(default=datetime.now, blank=False)
    likes = models.ManyToManyField(User, related_name='diary_publication')
    add_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('publication-detail', args=(str(self.id)))
        return reverse('home')

    def count_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    vk_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    linked_in_url = models.CharField(max_length=255, null=True, blank=True)
    telegram_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    publication = models.ForeignKey(Publication, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.publication.title, self.name)
