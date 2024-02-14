from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Client(models.Model):

    name = models.CharField(max_length=150, verbose_name='ФИО')
    post = models.CharField(max_length=150, default='поставщик', verbose_name='пост')
    email = models.EmailField(verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE,)

    def __str__(self):
        return f'{self.post} ({self.name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

class Message(models.Model):
    topic = models.CharField(max_length=150, verbose_name='тема')
    body = models.TextField(verbose_name='тело сообщения')

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент', **NULLABLE,)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

class Settigs_message(models.Model):

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='клиент', **NULLABLE,)


    time = models.TimeField(**NULLABLE, verbose_name='время рассылки')
    status = models.CharField(**NULLABLE, verbose_name='статус')
    period = models.CharField(**NULLABLE, verbose_name='периодичность')

    def __str__(self):
        return f'{self.message} {self.status}'

    class Meta:
        verbose_name = 'настройки'
        verbose_name_plural = 'настройки'


