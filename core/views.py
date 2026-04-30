from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo, User


def create_todo(request):
    if request.method != 'POST':
        return redirect('core:index')

    title = request.POST.get('title', '').strip()
    if not title:
        return redirect('core:index')

    description = request.POST.get('description', '').strip()
    user, _ = User.objects.get_or_create(
        username='default',
        defaults={
            'email': 'default@example.com',
            'password': 'password',
            'bio': 'Default user',
        },
    )

    Todo.objects.create(title=title, description=description, user=user)
    return redirect('core:index')


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


def get_todo_by_id(request, todo_id):
    find_todo = Todo.objects.get(pk=todo_id)
    if not find_todo:
        return HttpResponse("Todo not found", status=404)
    return render(request, "detail.html", {"todo": find_todo})


def update_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        is_completed = request.POST.get('is_completed') == 'on'
        todo.title = title
        todo.description = description
        todo.priority = priority
        todo.is_completed = is_completed
        todo.save()
        return redirect('core:get_todo_by_id', todo_id=todo_id)
    return render(request, 'update.html', {'todo': todo})


def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('core:index')
    return render(request, 'delete.html', {'todo': todo})
