from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Task

class IndexView(generic.ListView):
  template_name = 'todo/index.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    return Task.objects.order_by('-due_date')
  

class DetailView(generic.DetailView):
  model = Task
  template_name = 'todo/details.html'


def edit(request, task_id):
  task = Task.objects.get(pk=task_id)
  return render(request, 'todo/edit.html', {'task': task})


def make_changes(request, task_id):
  task = get_object_or_404(Task, pk=task_id)

  task.task_text = request.POST["task_text"]
  task.due_date = request.POST["task_date"]
  task.importance = request.POST["importance"]
  task.save()

  return HttpResponseRedirect(reverse('todo:details', args=(task.id,))) 
