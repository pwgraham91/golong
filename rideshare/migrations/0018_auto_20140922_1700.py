# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0017_traveler_traveler_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_picture',
            name='subject_car',
        ),
        migrations.DeleteModel(
            name='Car_Picture',
        ),
        migrations.RemoveField(
            model_name='traveler_picture',
            name='subject_traveler',
        ),
        migrations.DeleteModel(
            name='Traveler_Picture',
        ),
    ]
