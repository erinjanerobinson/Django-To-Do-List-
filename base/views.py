from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from .models import task 


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


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


class TaskUpdate(UpdateView):
    model = task 
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = task
    # changes the name in template from 'object2' to 'task'
    context_object_name = 'task'
    # if the form is submitted correctly directs the user to our task_list template 
    success_url = reverse_lazy('tasks')
    # renames template from 'task_confirm_delete' to 'task_delete'
    template_name = 'base/task_delete.html'

    