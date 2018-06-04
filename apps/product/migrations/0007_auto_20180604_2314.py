# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('product', '0006_auto_20180604_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc_pl',
        ),
        migrations.AddField(
            model_name='product',
            name='descript_en',
            field=cms.models.fields.PlaceholderField(related_name='product_descript_en', slotname=b'descript_en', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='descript_pl',
            field=cms.models.fields.PlaceholderField(related_name='product_descript_pl', slotname=b'descript_pl', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
