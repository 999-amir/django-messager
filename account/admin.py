from django.contrib import admin
from django.contrib.auth.models import Group
from .forms.costume_user import CostumeUserCreationForm, CostumeUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CostumeUser


class CostumeUserAdmin(UserAdmin):
    form = CostumeUserChangeForm
    add_form = CostumeUserCreationForm

    list_display = ('username', 'color', 'is_active', 'is_admin', 'last_login')
    list_filter = ('is_active', 'is_admin')
    fieldsets = (
        (
            'USER',
            {'fields': ('username', 'color', 'password')}
        ),
        (
            'USER-PERMISSIONS',
            {'fields': ('is_active', 'is_admin')}
        ),
        (
            'DATE',
            {'fields': ('last_login', 'updated', 'created')}
        )
    )
    add_fieldsets = (
        (
            'CREATE-USER',
            {'fields': ('username', 'password')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username', 'last_login', 'created')
    filter_horizontal = ()
    readonly_fields = ('last_login', 'updated', 'created')


admin.site.unregister(Group)
admin.site.register(CostumeUser, CostumeUserAdmin)
