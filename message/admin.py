from django.contrib import admin
from .models import *


@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated', 'created')
    ordering = ('-updated', '-created')
    readonly_fields = ('updated', 'created')
    search_fields = ('name', 'user')
    filter_horizontal = ('user',)


@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('group', 'user', 'created')
    ordering = ('-created',)
    readonly_fields = ('updated', 'created')
    search_fields = ('group', 'user')
