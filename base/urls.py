from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoItems.as_view(), name='home' ),
    path('todo/<name>/', views.TodoDetail.as_view(), name="todo"),
    path('todo_add/', views.CreateTodo.as_view(), name="todo_add"),
    path('update_todo/<name>/', views.UpdateTodo.as_view(), name="update_todo"),
    path('delete_todo/<name>/', views.DeleteTodo.as_view(), name="delete_todo"),
]