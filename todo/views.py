# views.py in your todo app

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def todo_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:  # make sure the title is not empty
            Todo.objects.create(title=title)
            if request.htmx:
                todos = Todo.objects.all().order_by('-created_at')
                return render(request, 'todo/todo-list.html', {'todos': todos})
        return HttpResponseRedirect(request.path_info)

    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todo/todo.html', {'todos': todos})  # make sure todo.html is being used correctly


def toggle_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    if request.htmx:
        return render(request, 'todo/todo_item.html', {'todo': todo})
    return redirect('todo_list')
