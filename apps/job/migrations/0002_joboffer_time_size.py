# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='time_size',
            field=models.CharField(default=datetime.datetime(2018, 5, 6, 9, 4, 5, 785035, tzinfo=utc), max_length=200, verbose_name=b'Wielkosc etatu'),
            preserve_default=False,
        ),
    ]
