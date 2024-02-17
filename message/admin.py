from django.contrib import admin

from message.models import Client, Message, SettigsMessage


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'post',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('topic', 'client',)
    list_filter = ('topic', 'client',)

@admin.register(SettigsMessage)
class Settigs_messageAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'message',)
    list_filter = ('client', 'status',)