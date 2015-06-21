# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('waypoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reportCategory', models.CharField(max_length=1, choices=[(b'1', b'corpse'), (b'2', b'injured'), (b'3', b'haven'), (b'3', b'firstaid')])),
                ('reportDetails', models.CharField(max_length=32)),
                ('reportGeometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('reportDate', models.DateTimeField(auto_now_add=True)),
                ('reporter', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
