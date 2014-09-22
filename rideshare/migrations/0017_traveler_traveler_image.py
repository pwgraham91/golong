# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0016_auto_20140922_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='traveler_image',
            field=models.ImageField(null=True, upload_to=b'traveler_images', blank=True),
            preserve_default=True,
        ),
    ]
