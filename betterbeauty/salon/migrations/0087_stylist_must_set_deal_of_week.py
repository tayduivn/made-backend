# Generated by Django 2.1 on 2019-01-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0086_change_default_tax_and_card_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylist',
            name='must_set_deal_of_week',
            field=models.BooleanField(default=False),
        ),
    ]
