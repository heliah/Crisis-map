# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('waypoints', '0003_remove_report_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='reportCategory',
            field=models.CharField(blank=True, max_length=1, choices=[(b'1', b'corpse'), (b'2', b'injured'), (b'3', b'haven'), (b'3', b'firstaid')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='reportDetails',
            field=models.CharField(max_length=32, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='reportGeometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, blank=True),
            preserve_default=True,
        ),
    ]
