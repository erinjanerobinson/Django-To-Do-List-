from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import task 


class TaskList(ListView):
    model = task
    # renames "object_list"  
    context_object_name = 'tasks'


class TaksDetail(DetailView):
    model = task
    # renames "object"
    context_object_name = 'task'
    # changes template name from "task_detail.html" to "task.html"
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = task
    # creates a form with all our model fields 
    fields = '__all__'
    # if the form is submitted correctly directs the user to our task_list template 
    success_url = reverse_lazy('tasks')
    