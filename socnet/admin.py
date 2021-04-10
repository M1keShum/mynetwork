from django.contrib import admin
from .models import Users, Messages


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sname', 'birthday')
    list_display_links = ('name', 'sname')
    search_fields = ('name', 'sname')


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'published')
    list_display_links = ('user',)
    search_fields = ('user', 'message')


admin.site.register(Users, UsersAdmin)
admin.site.register(Messages, MessagesAdmin)
