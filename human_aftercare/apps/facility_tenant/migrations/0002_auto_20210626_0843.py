# Generated by Django 3.2.4 on 2021-06-26 08:43

import apps.facility_tenant.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility_tenant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.facility_tenant.models.resident_photo_file_path_func),
        ),
        migrations.AddField(
            model_name='resident',
            name='photo_thumb',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to=apps.facility_tenant.models.resident_photo_thumb_file_path_func),
        ),
    ]
