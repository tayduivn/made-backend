# Generated by Django 2.0.3 on 2018-07-03 15:29

from django.db import migrations
import phonenumbers

def set_validated_phonenumber(apps, schema_editor):
    User = apps.get_model("core", "User")
    for user in User.objects.all():
        phone_number_to_save = None
        try:
            phonenumber_object = phonenumbers.parse(user.phone, "US")
            if phonenumbers.is_possible_number(phonenumber_object):
                phone_number_to_save = phonenumbers.format_number(
                    phonenumber_object, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            pass
        user.phone = phone_number_to_save
        user.save(update_fields=["phone"])

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20180622_1436'),
    ]

    operations = [
        migrations.RunPython(set_validated_phonenumber, migrations.RunPython.noop),
    ]