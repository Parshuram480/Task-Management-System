from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
# from django.http import HttpResponse
# from django.template import loader
from .forms import AddTaskForm


# Define view function for the Home page
@login_required
def home(request):
    return render(request, 'home.html')


def login_page(request):
    # CHeck the method is POST
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")

        # check the user exists or not with provided username
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid USer")
            return redirect('/login/')

        # AUthenticate the USER
        user = authenticate(username=username, password=password)

        # Checking the password is matched or not
        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home/')

    return render(request, "login.html")


def register_page(request):
    # check the request method is post
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check that the user exists with the same username
        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        # creating the user
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # saving the password in the user
        user.set_password(password)
        user.save()

        messages.info(request, "account created successfully!")
        return redirect('/login/')

    return render(request, "register.html")


def logout_view(request):
    logout(request)
    
    
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task.html')
    else:
        form = AddTaskForm()
    return render(request, 'add_task.html', {'form': form})
