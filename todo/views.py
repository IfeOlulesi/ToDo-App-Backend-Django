from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import Task
from .serializers import TaskSerializer

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


class TaskListApiView(APIView):
  premission_classes = permissions.IsAuthenticated

  # List all tasks
  def get(self, request, *args, **kwargs):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request, *args, **kwargs):
    print(request)
    data = {
      'task_text': request.data.get('task_text'), 
      'creation_date': request.data.get('creation_date'), 
      'due_date': request.data.get('due_date'), 
      'importance': request.data.get('importance'), 
      'user': request.user.id 
    }

    serializer = TaskSerializer(data=data)

    if serializer.isValid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)