# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180503_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc_en',
            field=cms.models.fields.PlaceholderField(related_name='product_desc_en', slotname=b'desc_en', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc_pl',
            field=cms.models.fields.PlaceholderField(related_name='product_desc_pl', slotname=b'desc_pl', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
