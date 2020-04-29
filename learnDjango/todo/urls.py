from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='addTodo'),
    path('complete/<todo_id>', views.complete, name='completeTodo'),
    path('deleteCompleted', views.deleteCompleted, name='deleteCompleted'),
    path('deleteAll', views.deleteAll, name='deleteAll')
]
