from django.shortcuts import render
from .serializer import TodoListSerializer
from .models import TodoList
from rest_framework import viewsets, generics


# Create your views here.
class TodoListView(generics.ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoListCreate(generics.CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoListDelete(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class UpdateStatusSerializer(generics.UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer