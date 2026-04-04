from django.http import HttpResponse


def create_todo(request):
    return HttpResponse("Create a new todo")


def get_todos(request):
    return HttpResponse("Get all todos")


def get_todo_by_id(request, todo_id):
    return HttpResponse(f"Get a todo by id and the todo  id is :{todo_id}")


def update_todo(request):
    return HttpResponse("Update a todo")


def delete_todo(request):
    return HttpResponse("updated delete a todo")