# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0010_auto_20140922_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_image',
            field=models.ImageField(default=b'car_images/default_car.jpg', upload_to=b'car_images', blank=True),
        ),
    ]
