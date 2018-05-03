# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('product', '0003_auto_20180422_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='spprzyg_en',
            field=cms.models.fields.PlaceholderField(related_name='createed_example_en', slotname=b'sposob przygotowania en', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='spprzyg_pl',
            field=cms.models.fields.PlaceholderField(related_name='createed_example_pl', slotname=b'sposob przygotowania pl', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
