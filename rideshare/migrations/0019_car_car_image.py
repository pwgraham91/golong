# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0018_auto_20140922_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(null=True, upload_to=b'car_images', blank=True),
            preserve_default=True,
        ),
    ]
