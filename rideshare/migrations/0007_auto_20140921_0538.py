# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0006_auto_20140921_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(null=True, upload_to=b'car_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='traveler',
            name='traveler_image',
            field=models.ImageField(null=True, upload_to=b'traveler_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='car',
            name='car_name',
            field=models.CharField(help_text=b'ex: Mr.T, Batmobile, Herbie, Green Hornet, Mystery Machine, Mad Max, Knight Rider', max_length=20),
        ),
    ]
