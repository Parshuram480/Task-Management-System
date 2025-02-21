from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AddTask
from .forms import AddTaskForm


# Define view function for the Home page
def home(request):
    return render(request, 'home.html')


# login page function
def login_page(request):
    # CHeck the method is POST
    if request.method == "POST":
        username = request.POST.get("username")
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
            return redirect('/task_list/')

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


# ask list page
@login_required
def task_list(request):
    # giving the authorization to the valid user 
    tasks = AddTask.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/task_list/')
    else:
        form = AddTaskForm()

    return render(request, 'add_task.html', {'form': form})


@login_required
def update_task(request, task_id):
    task = get_object_or_404(AddTask, id=task_id, user=request.user)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/task_list/')
    else:
        form = AddTaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(AddTask, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})


@login_required
def toggle_task_status(request, task_id):
    task = get_object_or_404(AddTask, id=task_id, user=request.user)
    task.status = 1 if task.status == 2 else 2
    task.save()
    return redirect('/task_list/')
