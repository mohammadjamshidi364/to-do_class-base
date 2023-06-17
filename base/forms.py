from django import forms

from .models import *



class AddTodo(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
