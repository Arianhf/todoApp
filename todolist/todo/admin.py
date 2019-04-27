from django.contrib import admin

from . import models

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created")

class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Group, GroupAdmin)
