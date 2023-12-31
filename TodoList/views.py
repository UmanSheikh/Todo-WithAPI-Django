from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from apis.models import TodoList

def home(request):
    todo_items = TodoList.objects.all()
    return render(request, 'home.html', {'todo_items': todo_items})


        