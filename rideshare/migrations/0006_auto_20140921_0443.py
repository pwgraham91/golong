# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0005_auto_20140920_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='end_latitude',
        ),
        migrations.RemoveField(
            model_name='route',
            name='end_longitude',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_latitude',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_longitude',
        ),
    ]
