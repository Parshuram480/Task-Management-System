from django.contrib import admin
from django.urls import path
from usertask.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', home, name="home"),
    # path('admin/', admin.site.urls),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('home/', logout_view, name="logout"),
    path('add_task/', add_task, name="add_task")
]
