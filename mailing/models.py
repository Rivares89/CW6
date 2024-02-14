from django.db import models

class Mailing(models.Model):
    PENDING = 'PD'
    SUCCESSFUL = 'SC'
    FAILED = 'FD'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESSFUL, 'Successful'),
        (FAILED, 'Failed'),
    ]

    topic = models.ForeignKey('message.Message', on_delete=models.CASCADE, verbose_name='сообщение')
    recipients = models.ManyToManyField('recipients.Recipients', verbose_name='адрес')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING, verbose_name='статус')

    created_at = models.DateTimeField(auto_now_add=True)
    send_at = models.DateTimeField(verbose_name='время рассылки')

    def __str__(self):
        return f'{self.topic} {self.created_at}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

