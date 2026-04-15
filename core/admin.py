from django.contrib import admin
<<<<<<< HEAD
from . import models


class userAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "password", "bio")


class TododAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "is_completed",
        "priority",
        "user",
        "created_at",
    )


# Register your models here.
admin.site.register(models.User, userAdmin)
admin.site.register(models.Todo, TododAdmin)
=======

from . import models

class userAdmin(admin.ModelAdmin):
    list_display = ("username","email","bio")

class todoAdmin(admin.ModelAdmin):
    list_display=("title","description","is_completed","priority","user","created_at")


admin.site.register(models.User, userAdmin)
admin.site.register(models.Todo, todoAdmin)

>>>>>>> 1fd8205064243d58b6a451d2d85f1e41afd9e63c
