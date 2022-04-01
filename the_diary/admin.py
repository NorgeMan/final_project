from django.contrib import admin
from .models import Publication, Category, Profile, Comment

admin.site.register(Publication)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
