from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from .models import Sending

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_hourly_messages, 'interval', hours=1)
    scheduler.add_job(send_daily_messages, 'interval', days=1)
    scheduler.add_job(send_weekly_messages, 'interval', weeks=1)
    scheduler.start()

def send_hourly_messages():
    send_messages(Sending.HOURLY)

def send_daily_messages():
    send_messages(Sending.DAILY)

def send_weekly_messages():
    send_messages(Sending.WEEKLY)

def send_messages(period):

    sendings = Sending.objects.filter(status=Sending.PENDING, period=period)

    for sending in sendings:
        send_mail(
            sending.topic.topic,
            sending.topic.body,
            'your_email@example.com',
            [sending.client.email],
        )
        sending.status = Sending.SUCCESSFUL
        sending.save()
