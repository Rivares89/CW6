from django.conf import settings
from django.core.mail import send_mail, EmailMessage, BadHeaderError

from mailing.models import Mailing


def send_letter(mailing_item):
    recipients = mailing_item.recipients.values_list('email', flat=True)

    email = EmailMessage(
        'Рассылочка',
        str(mailing_item.topic),  # Убедитесь, что тема (topic) представляет собой строку
        settings.EMAIL_HOST_USER,
        recipients
    )

    try:
        email.send(fail_silently=False)
        mailing_item.status = Mailing.SUCCESSFUL
    except BadHeaderError:
        mailing_item.status = Mailing.FAILED
        print('Invalid header found.')
    except Exception as e:
        mailing_item.status = Mailing.FAILED
        print(f'An error occurred: {e}')

    mailing_item.save()

