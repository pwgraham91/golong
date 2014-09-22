# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rideshare', '0011_auto_20140922_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'car_images', blank=True)),
                ('subject_car', models.OneToOneField(related_name=b'car_pictures', to='rideshare.Car')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Traveler_Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'traveler_images', blank=True)),
                ('subject_traveler', models.OneToOneField(related_name=b'traveler_pictures', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='traveler_image',
        ),
    ]
