"""views.py """

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm

# Create your views here.

def count_closed_task():

    tasks = Task.objects.all()
    closed_task = 0
    now = timezone.localtime()

    for task in tasks:
        if task.deadline and task.deadline < now:
            closed_task += 1 
    return closed_task

def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            #return redirect('task_detail', pk=task.pk)
            return redirect('todo_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo_manager/update.html', {'form': form, 'closed_task':count_closed_task()})


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            #return redirect('task_detail', pk=task.pk)
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todo_manager/update.html', {'form': form, 'closed_task':count_closed_task()})


def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('todo_list')

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_manager/todo_list.html', {'tasks':tasks, 'closed_task':count_closed_task()})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_manager/task_detail.html', {'task':task})


def toggle_finished(request, pk):

    task = get_object_or_404(Task, pk=pk)

    if task:
        task.finished = not task.finished
        task.save()
    
    return redirect('..')