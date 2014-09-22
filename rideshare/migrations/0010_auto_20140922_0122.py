# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0009_auto_20140922_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traveler',
            name='traveler_image',
            field=models.ImageField(default=b'traveler_images/default.jpg', upload_to=b'traveler_images', blank=True),
        ),
    ]
