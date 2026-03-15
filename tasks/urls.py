from django.urls import path
from . import views

urlpatterns = [
    # Task URLs
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/status/', views.update_task_status, name='update-task-status'),
]
