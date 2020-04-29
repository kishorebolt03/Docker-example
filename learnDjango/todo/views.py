from django.shortcuts import render, redirect
from .models import Todo
from .forms import addTodoForm, newTodoForm
from django.views.decorators.http import require_POST

def index(request):
    todo_list = Todo.objects.order_by('id')
    # form = addTodoForm()
    form = newTodoForm()

    context = { 'todo_list' : todo_list,
    'form' : form }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    # form = addTodoForm(request.POST)
    form = newTodoForm(request.POST)

    print(request.POST['text'])
    if form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        new_todo = form.save()
    return redirect('index')

def complete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    print(Todo.objects.filter(complete__exact=True).delete())
    return redirect('index')

def deleteAll(request):
    print(Todo.objects.all().delete())
    return redirect('index')