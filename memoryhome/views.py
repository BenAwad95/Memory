from django.db import models
from django.shortcuts import render
from .models import Memory
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

class MemoryCreate(CreateView):
    model = Memory
    fields = '__all__'
    success_url = reverse_lazy('memoryhome:memory_create')

class MemoryDetail(DetailView):
    model = Memory
    context_object_name = 'memory'

class MemoryList(ListView):
    model = Memory

class MemoryUpdate(UpdateView):
    model = Memory

class MemoryDelete(DeleteView):
    model = Memory

