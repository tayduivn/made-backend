# Generated by Django 2.0.3 on 2018-04-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180421_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('stylist', 'Stylist'), ('staff', 'Staff')], max_length=10),
        ),
    ]
