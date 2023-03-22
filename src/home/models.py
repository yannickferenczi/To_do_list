from django.db import models
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from accounts.models import MyCustomUser


class ToDoList(models.Model):
    todolist_owner = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    # @property
    # def todolist_owner(self):
    #     return self.request.user

    def get_absolute_url(self):
        return reverse('home')


class Item(models.Model):
    todolist_name = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    deadline = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.description}({self.todolist_name})"
