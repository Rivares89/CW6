from django.contrib.auth.models import AbstractUser
from django.db import models

from message.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)


    email_verify = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
