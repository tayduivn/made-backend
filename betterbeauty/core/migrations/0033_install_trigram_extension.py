# Generated by Django 2.1 on 2018-10-11 16:42
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20181011_1209'),
    ]

    operations = [
        TrigramExtension()
    ]