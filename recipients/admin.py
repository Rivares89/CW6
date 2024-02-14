from django.contrib import admin
from recipients.models import Recipients


@admin.register(Recipients)
class RecipientsAdmin(admin.ModelAdmin):
    list_display = ('email', 'name',)

