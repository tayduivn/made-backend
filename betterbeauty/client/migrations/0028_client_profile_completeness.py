# Generated by Django 2.1 on 2018-11-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0027_client_has_seen_educational_screens'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='profile_completeness',
            field=models.FloatField(default=0.0, blank=True, null=True),
        ),
    ]
