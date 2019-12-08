# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20180604_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='meta_description_en',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Opis strony w metatagu EN'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description_pl',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Opis strony w metatagu PL'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title_en',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Tytu\xc5\x82 strony w meta tagu EN'),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title_pl',
            field=models.CharField(default=b'', max_length=255, verbose_name=b'Tytu\xc5\x82 strony w meta tagu PL'),
        ),
    ]
