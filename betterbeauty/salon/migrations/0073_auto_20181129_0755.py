# Generated by Django 2.1 on 2018-11-29 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0072_stylistspecialavailabledate'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stylistspecialavailabledate',
            unique_together={('stylist', 'date')},
        ),
        migrations.AlterModelTable(
            name='stylistspecialavailabledate',
            table='stylist_special_available_date',
        ),
    ]
