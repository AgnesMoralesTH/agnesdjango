from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
# Create your views here.
class Home(TemplateView):
    template_name = "base/home.html"

class Shop(TemplateView):
    template_name = "base/shop.html"

class Contact(TemplateView):
    template_name = "base/contact.html"

class MessageCreate(CreateView):
    model = Contact
    fields = ['name','email','topic','description']
    template_name = 'base/contact.html'
    success_url = reverse_lazy('home')



   