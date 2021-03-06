# Generated by Django 2.1 on 2019-01-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0084_auto_20190118_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylist',
            name='card_fee',
            field=models.DecimalField(decimal_places=4, default=0.0275, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stylist',
            name='tax_rate',
            field=models.DecimalField(decimal_places=4, default=0.045, max_digits=5),
        ),
    ]
