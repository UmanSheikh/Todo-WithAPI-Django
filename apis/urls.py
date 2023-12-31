from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.TodoListView.as_view(), name = 'view'),
    path('create/', views.TodoListCreate.as_view(), name = 'create'),
    path('delete/<int:pk>/', views.TodoListDelete.as_view(), name = 'delete'),
    path('update/<int:pk>/', views.UpdateStatusSerializer.as_view(), name = 'update'),
]
