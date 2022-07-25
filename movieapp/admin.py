from django.contrib import admin

# Register your models here.
from movieapp.models import Movie

admin.site.register(Movie)