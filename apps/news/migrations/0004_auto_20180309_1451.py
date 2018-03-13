# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('news', '0003_auto_20180309_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content_en',
            field=cms.models.fields.PlaceholderField(related_name='news_content_en', slotname=b'content_en', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='content_pl',
            field=cms.models.fields.PlaceholderField(related_name='news_content_pl', slotname=b'content_pl', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
