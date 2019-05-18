"""views.py """

from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404

# Create your views here.

def update(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return todo_list(request)
    else:
        form = TaskForm()
    return render(request, 'todo_manager/update.html', {'form':form})


def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_manager/todo_list.html', {'tasks':tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_manager/task_detail.html', {'task':task})