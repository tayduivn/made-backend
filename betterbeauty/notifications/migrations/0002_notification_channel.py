# Generated by Django 2.1 on 2018-11-07 17:37

from django.db import migrations, models
import notifications.types


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='channel',
            field=models.CharField(choices=[('sms', 'SMS message'), ('push', 'Push Notification')], default=notifications.types.NotificationChannel('push'), max_length=16, null=True),
        ),
    ]
