from django.urls import path
from usertask import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('task_list/', views.task_list, name="task_list"),
    path('logout/', views.logout_view, name="logout"),
    path('task_list/add/', views.add_task, name="add_task"),
    path('task_list/update/<int:task_id>/', views.update_task, name="update_task"),
    path('task_list/delete/<int:task_id>/', views.delete_task, name="delete_task"),
    path('task_list/toggle/<int:task_id>/', views.toggle_task_status, name="toggle_task_status"),
]
