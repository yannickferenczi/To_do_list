from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.forms import UserChangeForm, MyCustomUserCreationForm
from accounts.models import MyCustomUser


@admin.register(MyCustomUser)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = MyCustomUserCreationForm

    list_display = (
        'email',
        'is_admin',
    )
    list_filter = ('is_admin', )
    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', )}),
    )
    add_fieldsets = (
        ('I definitely write whatever I want', {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.unregister(Group)
