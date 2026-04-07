from django.shortcuts import render,redirect
from django.contrib import messages
from . models import User,Todo
import json
#def dashboard(request):
#    user = request.session.get('user')
 #   if not user:
 #       return redirect('login')
 #   user = User.objects.get(id=user)

def get_todos(request):
    todos = Todo.objects.all().order_by("-created_at")
    return render(request,"todo_list.html" )
        

def create_todo(request):
    if request.method == 'POST':
        data=json(request.body)
        print(data)
        Todo.objects.create(
            title = data.get('title'),
            description = data.get('description'),
            created_at = data.get('created_at'),
            PRIORITY = data.get('PRIORITY', 'M')
        )
        
    return render(request,"create_list.html")




def get_todo_by_id(request,todo_id):
    return redirect("get_todos")