from django.contrib import admin
from django.urls import path
from usertask.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('task_list/', task_list, name="task_list"),
    path('logout/', logout_view, name="logout"),
    path('task_list/add/', add_task, name="add_task"),
    path('task_list/update/<int:task_id>/', update_task, name="update_task"),
    path('task_list/delete/<int:task_id>/', delete_task, name="delete_task"),
    path('task_list/toggle/<int:task_id>/', toggle_task_status, name="toggle_task_status"),
]
