from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
  # Ex: todo/
  path('', views.index, name='index'),

  # Ex: todo/2   --to view details
  path('<int:task_id>/', views.details, name='details'),
  
  # Ex: todo/2/edit
  path('<int:task_id>/edit', views.edit, name='edit'),
  
  # Ex: todo/2/make_changes
  path('<int:task_id>/make_changes', views.make_changes, name='make_changes'),
  
  # Ex: todo/add_task
  path('add_task/', views.add_task, name='add_task'),
]