from django.contrib import admin

from message.models import Client, Message, Settigs_message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'post',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('topic', 'client',)
    list_filter = ('topic', 'client',)

@admin.register(Settigs_message)
class Settigs_messageAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'message',)
    list_filter = ('client', 'status',)