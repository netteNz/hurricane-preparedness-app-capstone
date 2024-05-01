# todo/urls.py

from django.urls import path
from . import views

app_name = 'todo'  # Define the application namespace

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_list, name='create_todo'),  # Assumed to handle creation via POST
    path('toggle/<int:pk>/', views.toggle_todo, name='toggle_todo'),
]
