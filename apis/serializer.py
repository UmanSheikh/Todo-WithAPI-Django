from rest_framework import serializers
from .models import TodoList

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
    
class UpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['status']