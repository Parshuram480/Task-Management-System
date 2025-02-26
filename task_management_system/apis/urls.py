from django.urls import path
from .views import register_api, login_api, logout_api, task_list_api, add_task_api, update_task_api, delete_task_api, toggle_task_api

urlpatterns = [
    path('login/', login_api, name='api-login'),
    path('register/', register_api, name='api-register'),
    path('logout/', logout_api, name='api-logout'),
    path('tasks/', task_list_api, name='api-task-list'),
    path('tasks/add/', add_task_api, name='api-add-task'),
    path('tasks/update/<int:task_id>/', update_task_api, name='api-update-task'),
    path('tasks/delete/<int:task_id>/', delete_task_api, name='api-delete-task'),
    path('tasks/toggle/<int:task_id>/', toggle_task_api, name='api-toggle-task'),
]
