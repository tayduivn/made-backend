# Generated by Django 2.1 on 2019-02-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0033_auto_20190207_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylistsearchrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
