from django import forms
from django.contrib import admin

from .models import Type, Breed, Pet

admin.site.register(
    (Type, Breed, Pet)
)
