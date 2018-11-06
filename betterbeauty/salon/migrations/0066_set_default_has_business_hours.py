# Generated by Django 2.1 on 2018-11-01 12:01
from django.contrib.gis.db.backends.postgis.schema import PostGISSchemaEditor
from django.db import migrations
from django.db.migrations.state import StateApps


def set_default_has_business_hours(apps: StateApps, schema_editor: PostGISSchemaEditor):
    Stylist = apps.get_model('salon', 'Stylist')
    stylists = Stylist.objects.all()
    for stylist in stylists.iterator():
        has_business_hours_set=stylist.available_days.filter(
            is_available=True,
            work_start_at__isnull=False,
            work_end_at__isnull=False
        ).exists()
        if has_business_hours_set:
            stylist.has_business_hours_set=True
            stylist.save()



class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0065_stylist_has_business_hours_set'),
    ]

    operations = [
        migrations.RunPython(code=set_default_has_business_hours, reverse_code=migrations.RunPython.noop)
    ]