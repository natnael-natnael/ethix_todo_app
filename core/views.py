from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo, User


def create_todo(request):
    return HttpResponse("Create a new todo")


def get_todos(request):
    todos = Todo.objects.all()
    newtodos = []
    for todo in todos:
        newtodos.append(
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "user": todo.user.username,
            }
        )
    print(newtodos)
    return render(request, "index.html", {"todo_lists": newtodos})


def get_todo_by_id(request, id):
    todo = Todo.objects.get(pk=id)
    return HttpResponse(f" todo title:{todo.title} description : {todo.description}")


def update_todo(request):
    return HttpResponse("Update a todo")


def delelte_todo(request):
    return HttpResponse("Delete a todo")
