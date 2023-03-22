from django.contrib import admin

from home.models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'todolist_owner',
    )

    fieldsets = (
        (None, {'fields': ('name', )}),
    )
    add_fieldsets = (
        (None, {'fields': ('name', 'todolist_owner', ), }),
    )
