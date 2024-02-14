from django.db import models

class Recipients(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'