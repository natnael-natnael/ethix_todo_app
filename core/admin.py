from django.contrib import admin
from .models import Todo, User

# Register your models here.
admin.site.site_header = "Ethix Todo App Admin"
admin.site.site_title = "Ethix Todo App Admin Portal"

admin.site.register(User)
admin.site.register(Todo)