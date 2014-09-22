# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(help_text=b'Format should be: 650-111-2222', max_length=12, null=True)),
                ('age', models.IntegerField(max_length=2, null=True)),
                ('background_checked', models.BooleanField(default=False)),
                ('driver', models.BooleanField(default=False, help_text=b'Driver= True, Rider= False')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_name', models.CharField(help_text=b'ex: Mr.T, Batmobile, Herbie, Green Hornet, Mystery Machine, Mad Max, Knight Rider, ', max_length=20)),
                ('car_model', models.CharField(help_text=b'ex: Gray Nissan Altima', max_length=40)),
                ('car_year', models.CharField(help_text=b'ex: 2008', max_length=4)),
                ('seats', models.SmallIntegerField()),
                ('owner', models.ForeignKey(related_name=b'cars', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_name', models.CharField(max_length=30)),
                ('start_city_state', models.CharField(max_length=50)),
                ('start_latitude', models.FloatField(null=True)),
                ('start_longitude', models.FloatField(null=True)),
                ('end_city_state', models.CharField(max_length=50)),
                ('end_latitude', models.FloatField(null=True)),
                ('end_longitude', models.FloatField(null=True)),
                ('passenger', models.ManyToManyField(related_name=b'route_passengers', to=settings.AUTH_USER_MODEL)),
                ('trip_car', models.ForeignKey(related_name=b'route_car', to='rideshare.Car')),
                ('trip_driver', models.ForeignKey(related_name=b'route_driver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
