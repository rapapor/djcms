# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180421_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_big',
            field=models.ImageField(help_text='sugerowana wielkosc 870x412', upload_to=b'media/aktualnosci/', null=True, verbose_name=b'zdjecie duze do tresci', blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='image_start',
            field=models.ImageField(help_text='sugerowana wielkosc 760x612', upload_to=b'media/aktualnosci/', null=True, verbose_name=b'zdjecie na pierwsza strone', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=b'media/aktualnosci/', null=True, verbose_name=b'zdjecie na liste newsow', blank=True),
        ),
    ]
