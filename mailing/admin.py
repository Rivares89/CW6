from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('topic', 'get_emails', 'created_at', )
    list_filter = ('topic', )

    def get_emails(self, obj):
        return ", ".join([recipients.email for recipients in obj.recipients.all()])

    get_emails.short_description = 'Emails'