# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0013_auto_20140922_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_picture',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/car_images'),
        ),
        migrations.AlterField(
            model_name='traveler_picture',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media/traveler_images'),
        ),
    ]
