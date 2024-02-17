# Generated by Django 4.2 on 2024-02-14 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_message_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettigsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True, verbose_name='время рассылки')),
                ('status', models.CharField(blank=True, max_length=50, null=True, verbose_name='статус')),
                ('period', models.CharField(blank=True, max_length=50, null=True, verbose_name='периодичность')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='message.client', verbose_name='клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='message.message', verbose_name='сообщение')),
            ],
            options={
                'verbose_name': 'настройки',
                'verbose_name_plural': 'настройки',
            },
        ),
        migrations.DeleteModel(
            name='Settigs_message',
        ),
    ]
