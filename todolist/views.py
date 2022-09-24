import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.models import Task

@login_required(login_url='/todolist/login')
def home(request):
    tasks = Task.objects.all()
    context = {
        'name': 'Daniel Christian Mandolang',
        'npm': '2106630006',
        'tasks': tasks
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login')
def create_task(request):
    return render(request, 'create_task.html')

@login_required(login_url='/todolist/login')
def create(request):
    if (request.method == 'POST'):
        # TODO: Get data from form
        # TODO: Create new instance
        form = request.POST.dict()
        if (form.is_valid()):
            print("HERE")
        return HttpResponseRedirect(reverse('todolist:'))

@login_required(login_url='/todolist/login')
def mark_done(request, id):
    task = Task.objects.filter(pk=id)
    task.done = not task.done
    task.save()
    HttpResponseRedirect(reverse('todolist:'))

@login_required(login_url='/todolist/login')
def delete(request, id):
    Task.objects.delete(pk=id)
    HttpResponseRedirect(reverse('todolist:'))

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:home"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response