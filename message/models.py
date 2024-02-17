from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):

    name = models.CharField(max_length=150, verbose_name='ФИО')
    post = models.CharField(max_length=150, default='поставщик', verbose_name='пост')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE,)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=150, verbose_name='тема')
    body = models.TextField(verbose_name='тело сообщения')

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE,)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

class SettigsMessage(models.Model):

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='клиент', **NULLABLE,)


    time = models.TimeField(**NULLABLE, verbose_name='время рассылки')
    status = models.CharField(**NULLABLE, max_length=50, verbose_name='статус')
    period = models.CharField(**NULLABLE, max_length=50, verbose_name='периодичность')

    def __str__(self):
        return f'{self.message} {self.status}'

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'

class Sending(models.Model):
    PENDING = 'PD'
    SUCCESSFUL = 'SC'
    FAILED = 'FD'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESSFUL, 'Successful'),
        (FAILED, 'Failed'),
    ]
    HOURLY = 'EH'
    DAILY = 'ED'
    WEEKLY = 'EW'
    PERIOD_CHOICES = [
        (HOURLY, 'Hoyrly'),
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    ]

    topic = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='клиент', **NULLABLE,)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING, verbose_name='статус')
    period = models.CharField(max_length=2, choices=PERIOD_CHOICES, default=WEEKLY, verbose_name='период')

    created_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(verbose_name='время рассылки')

    def __str__(self):
        return f'{self.topic} {self.created_at}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


