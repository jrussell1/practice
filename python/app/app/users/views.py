from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'users/home.html', {
        "name": "Susie Student",
        "tasks": ["Thing 1", "Thing 2", "Thing 3"]
    })

def detail(request):
    return render(request, 'users/detail.html', {})

def add(request):
    return render(request, 'users/add.html', {})