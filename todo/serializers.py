from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ['task_text', 'creation_date', 'due_date', 'importance', 'user']
