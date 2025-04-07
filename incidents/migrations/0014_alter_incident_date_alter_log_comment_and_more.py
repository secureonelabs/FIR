# Generated by Django 5.2 on 2025-04-07 22:06

import incidents.models
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0013_profile_light_mode_alter_incident_severity_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='date',
            field=models.DateTimeField(blank=True, default=incidents.models.datetimenow),
        ),
        migrations.AlterField(
            model_name='log',
            name='comment',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='incidents.comments'),
        ),
        migrations.AlterField(
            model_name='log',
            name='incident',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='incidents.incident'),
        ),
        migrations.AlterField(
            model_name='log',
            name='what',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='log',
            name='who',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
