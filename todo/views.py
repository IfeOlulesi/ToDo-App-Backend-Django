from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Task

def home(request):
  return render(request, "todo/welcome.html", {})

class IndexView(generic.ListView):
  template_name = 'todo/index.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    return Task.objects.order_by('-due_date')
  

class DetailView(generic.DetailView):
  model = Task
  template_name = 'todo/details.html'


def edit(request, pk): # who is sending pk to this functions ehn!!! - its supposed to be task_id
  # but its like someone is deliberately sending something like this:- edit(pk='blablabla')
  task_id = pk
  task = Task.objects.get(pk=task_id)
  return render(request, 'todo/edit.html', {'task': task})


def make_changes(request, pk):
  task_id = pk
  task = get_object_or_404(Task, pk=task_id)

  task.task_text = request.POST["task_text"]
  task.importance = request.POST["importance"]
  if request.POST["task_date"]:
    task.due_date = request.POST["task_date"]
  
  task.save()

  return HttpResponseRedirect(reverse('todo:details', args=(task.id,))) 
