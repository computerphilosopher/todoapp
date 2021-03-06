from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create', views.create, name='create'),
    path('toggle_finished/<int:pk>', views.toggle_finished, name='toggle_finished'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/edit/', views.update, name='update'),
    path('task/<int:pk>/delete', views.delete, name='delete'),
]