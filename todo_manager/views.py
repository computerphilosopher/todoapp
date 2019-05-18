"""views.py """

from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_manager/update.html', {'form': form})

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo_list')

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_manager/todo_list.html', {'tasks':tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_manager/task_detail.html', {'task':task})