from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing


def send_letter(mailing_item):
    recipients = mailing_item.recipients.values_list('email', flat=True)

    send_mail(
        'Рассылочка',
        str(mailing_item.topic),  # Убедитесь, что тема (topic) представляет собой строку
        settings.EMAIL_HOST_USER,
        recipients,
        fail_silently=False,  # Установите True, если вы не хотите получать исключения при ошибках отправки
    )

    )
