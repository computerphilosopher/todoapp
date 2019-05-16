"""views.py """

from django.shortcuts import render
from .models import Task

# Create your views here.

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo_manager/todo_list.html', {'tasks':tasks})
