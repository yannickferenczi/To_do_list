from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView


from home.models import ToDoList


class IndexView(ListView):
    model = ToDoList
    template_name = "home/todo_list.html"
    context_object_name = "todo_list"


class TodolistCreate(LoginRequiredMixin, CreateView):
    model = ToDoList
    template_name = "home/create.html"
    context_object_name = 'form'
    fields = (
        'name',
    )

    def form_valid(self, form):
        form.instance.todolist_owner = self.request.user
        return super().form_valid(form)

    # form_class = ToDoListForm

    # def get_form_kwargs(self):
    #     kwargs = super(TodolistCreate, self).get_form_kwargs()
    #     current_user = MyCustomUser.objects.get(email=self.request.user)
    #     kwargs['user'] = current_user.id
    #     return kwargs
