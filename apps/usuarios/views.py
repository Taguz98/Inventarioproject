from django.shortcuts import render
from django.views.generic import CreateView, ListView,\
    UpdateView, DetailView, DeleteView, View

from .models import *
# Create your views here.

class RegistratUsuario(CreateView):
    model = Usuario
    fields = ['nombre', 'apellido', 'cedula', 'email', 'password']
    success_url = '/usuarios/'
