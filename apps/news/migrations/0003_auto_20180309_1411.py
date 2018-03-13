# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='content_pl',
        ),
    ]
