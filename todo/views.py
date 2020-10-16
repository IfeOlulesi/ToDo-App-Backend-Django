from django.shortcuts import render
from django.http import HttpResponse

from .models import Task

def index(request):
  task_list = Task.objects.order_by('-due_date')
  return render(request, 'todo/index.html', {'task_list': task_list})

def details(request, task_id):
  task_obj = Task.objects.get(pk=task_id)
  return render(request, 'todo/details.html', {'task': task_obj})

def add_task(request):
  return HttpResponse("You are adding another task")