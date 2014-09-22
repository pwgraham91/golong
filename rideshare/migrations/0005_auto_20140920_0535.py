# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0004_auto_20140920_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
