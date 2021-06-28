# Generated by Django 3.2.4 on 2021-06-28 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility_tenant', '0003_auto_20210627_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='TherapyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('duration_minutes', models.PositiveIntegerField()),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='therapy_note_created', to=settings.AUTH_USER_MODEL, editable=False)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='therapy_note', to='facility_tenant.resident')),
                ('update_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='therapy_note_updated', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
    ]
