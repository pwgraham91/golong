# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0002_auto_20140919_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='end_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='start_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]
