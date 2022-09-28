from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def show_me(request):
    return render(request, 'me.html')