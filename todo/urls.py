from django.urls import path
from .views import todo, create_todo, mark_todo, delete_todo

app_name = 'todo'

urlpatterns = [
    path('', todo, name='todo'),
    path('create_todo/', create_todo, name='create_todo'),
    path('mark_todo/<int:pk>/', mark_todo, name='mark_todo'),
    path('delete_todo/<int:pk>/', delete_todo, name='delete_todo'),
]
