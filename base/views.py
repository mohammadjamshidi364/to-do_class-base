from typing import Any, Optional
from django.db import models
from django.http import Http404
from django.shortcuts import render , get_object_or_404 
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy


from .models import *
from .forms import *


class TodoItems(ListView):
    model = Todo
    template_name = 'base/home.html'
    context_object_name = 'todoItems'
    

class TodoDetail(DetailView):
    model = Todo
    template_name = 'base/todo.html'
    context_object_name = 'todo'
    
    
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        self.name = get_object_or_404(Todo , name=self.kwargs['name'])

        if self.name is not None:
            queryset = queryset.filter(name=self.name)

        # If none of those are defined, it's an error.
        if self.name is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                ("No %(verbose_name)s found matching the query")
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
        return obj
    

class CreateTodo(CreateView):
    model = Todo
    fields = ['name']
    template_name = 'base/add_todo.html'
    success_url = reverse_lazy('home')
    
    
class UpdateTodo(TodoDetail,UpdateView):
    
    model = Todo
    fields = ['name']
    template_name = "base/update_todo.html"
    success_url = reverse_lazy('home')
    
    
    def get_object(self, queryset=None):
        return super().get_object(queryset)

class DeleteTodo(TodoDetail,DeleteView):
    
    model = Todo
    fields = ['name']
    template_name = 'base/delete_todo.html'
    success_url = reverse_lazy('home')
    
    def get_object(self, queryset=None):
        return super().get_object(queryset)
        