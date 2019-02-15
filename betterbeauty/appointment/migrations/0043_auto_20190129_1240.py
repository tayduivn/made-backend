# Generated by Django 2.1 on 2019-01-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0042_auto_20190117_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='comment',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='rating',
            field=models.IntegerField(blank=True, choices=[('0', 0), ('1', 1)], default=None, null=True),
        ),
    ]