from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'todo'

urlpatterns = [
  # Ex: todo/
  path('', views.IndexView.as_view(), name='index'),

  # Ex: todo/2   --to view details
  path('<int:pk>/', views.DetailView.as_view(), name='details'),
  
  # Ex: todo/2/edit  --to edit the task
  path('<int:pk>/edit', views.edit, name='edit'),
  
  # Ex: todo/2/make_changes
  path('<int:pk>/make_changes', views.make_changes, name='make_changes'),
  
  # Ex: todo/add_task
  # path('add_task/', views.add_task, name='add_task'),

  # API
  path('api', views.TaskListApiView.as_view()),
]