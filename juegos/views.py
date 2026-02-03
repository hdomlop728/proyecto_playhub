from django.shortcuts import render
from .models import Juego
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class juego_list(LoginRequiredMixin, ListView):
    model = Juego
    template_name = 'juegos/juego_list.html'
    context_object_name ='juegos'

class juego_create(LoginRequiredMixin, CreateView):
    model = Juego
    fields = ['titulo', 'plataforma', 'precio', 'fecha_lanzamiento']
    template_name = 'juegos/juego_form.html'
    success_url = reverse_lazy('juego_list')
    extra_context = {'modo': 'crear'}

class juego_update(LoginRequiredMixin, UpdateView):
    model = Juego
    fields = ['titulo', 'plataforma', 'precio', 'fecha_lanzamiento']
    template_name = 'juegos/juego_form.html'
    success_url = reverse_lazy('juego_list')

class juego_delete(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = 'juegos/juego_delete.html'
    success_url = reverse_lazy('juego_list')
