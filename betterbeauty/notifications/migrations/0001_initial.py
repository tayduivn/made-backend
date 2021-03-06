# Generated by Django 2.1 on 2018-11-06 14:55

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import notifications.models
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('target', models.CharField(choices=[('client', 'Client'), ('stylist', 'Stylist')], max_length=16)),
                ('code', models.CharField(max_length=64, verbose_name='Notification code')),
                ('message', models.CharField(max_length=512)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=notifications.models.default_json_field_value)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('send_time_window_start', models.TimeField()),
                ('send_time_window_end', models.TimeField()),
                ('send_time_window_tz', timezone_field.fields.TimeZoneField(default='America/New_York')),
                ('pending_to_send', models.BooleanField()),
                ('sent_at', models.DateTimeField(null=True)),
                ('discard_after', models.DateTimeField()),
                ('device_acked_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
