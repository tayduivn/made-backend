# Generated by Django 2.0.3 on 2018-06-20 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0033_auto_20180619_0325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicetemplate',
            old_name='base_price',
            new_name='regular_price',
        ),
        migrations.RenameField(
            model_name='stylistservice',
            old_name='base_price',
            new_name='regular_price',
        ),
    ]