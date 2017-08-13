# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Belema',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=25, verbose_name='YOUR NAME')),
                ('skin_colour', models.CharField(max_length=300, verbose_name='SKIN COLOUR')),
                ('age', models.IntegerField()),
                ('instituition', models.CharField(max_length=30, verbose_name='SCHOOL ATTENDED')),
            ],
        ),
    ]
