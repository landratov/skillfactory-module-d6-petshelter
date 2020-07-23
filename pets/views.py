from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Pet


class PetList(ListView):
    model = Pet
    template_name = 'pet_list.html'


class PetDetail(DetailView):
    model = Pet
    template_name = 'pet_detail.html'


class Index(TemplateView):
    template_name = 'index.html'


class Contacts(TemplateView):
    template_name = 'contacts.html'