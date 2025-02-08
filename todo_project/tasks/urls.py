from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
]
