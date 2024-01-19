from mailing.models import Mailing


def send_letter(sett):
    item = Mailing.objects.get(pk=sett)
