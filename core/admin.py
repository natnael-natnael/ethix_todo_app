from django.contrib import admin

from . import models

class userAdmin(admin.ModelAdmin):
    list_display = ("username","email","bio")

class todoAdmin(admin.ModelAdmin):
    list_display=("title","description","is_completed","priority","user","created_at")


admin.site.register(models.User, userAdmin)
admin.site.register(models.Todo, todoAdmin)

