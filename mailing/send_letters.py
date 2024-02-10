import os
import django
from django.utils import timezone

from mailing.models import Mailing
from mailing.services import send_letter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()


def send_pending_letters():
    now = timezone.now()
    mailings_to_send = Mailing.objects.filter(status=Mailing.PENDING, send_at__lte=now)
    for mailing in mailings_to_send:
        send_letter(mailing)

if __name__ == "__main__":
    send_pending_letters()