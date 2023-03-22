from django import forms

from accounts.models import MyCustomUser
from home.models import ToDoList


class ToDoListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ToDoListForm, self).__init__(*args, **kwargs)
        self.fields['todolist_owner'] = forms.ModelChoiceField(queryset=MyCustomUser.objects.filter(pk=user))  # queryset=ToDoList.objects.filter(todolist_owner=user)
        # print(self.fields['todolist_owner'])

    class Meta:
        model = ToDoList
        fields = (
            'todolist_owner',
            'name',
        )
    #
    # def save(self, commit=True):
    #     # Docstring
    #     todolist = super().save(commit=False)
    #     todolist.todolist_owner_id = self.user_object.pk
    #     if commit:
    #         todolist.save()
    #     return todolist
