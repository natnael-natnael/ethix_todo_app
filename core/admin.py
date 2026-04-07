from django.contrib import admin

from . import models

class userAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password", "bio") 

class todoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "is_completed", "created_at", "priority", "user")

admin.site.register(models.User, userAdmin)
admin.site.register(models.Todo, todoAdmin)