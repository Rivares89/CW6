# Generated by Django 5.0.1 on 2024-01-17 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Logs_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=150, verbose_name='тема')),
                ('body', models.TextField(verbose_name='тело сообщения')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.client', verbose_name='клиент')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Settigs_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время рассылки')),
                ('status', models.CharField(blank=True, null=True, verbose_name='статус')),
                ('period', models.CharField(blank=True, null=True, verbose_name='периодичность')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='message.client', verbose_name='клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.message', verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'настройки',
                'verbose_name_plural': 'настройки',
            },
        ),
    ]
