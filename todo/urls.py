from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
  # Ex: todo/
  path('', views.index, name='index'),
  # Ex: todo/2
  path('<int:task_id>/', views.details, name='details'),
  # Ex: todo/add_task
  path('add_task/', views.add_task, name='add_task')
]