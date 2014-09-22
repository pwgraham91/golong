# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0003_auto_20140920_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]
