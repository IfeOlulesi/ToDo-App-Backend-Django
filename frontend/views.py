from django.shortcuts import render
from django.views import generic
# from django.http import HttpResponse

from todo.models import Task

class IndexView(generic.ListView):
  template_name = 'frontend/index.html'
  context_object_name = 'task_list'
  
  def get_queryset(self):
    return Task.objects.order_by('-due_date')
  

class DetailsView(generic.DetailView):
  model = Task
  template_name = 'frontend/details.html'


def add_task(request):
  return HttpResponse("You are adding another task")
