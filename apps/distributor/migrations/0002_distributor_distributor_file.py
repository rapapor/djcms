# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributor',
            name='distributor_file',
            field=models.ImageField(upload_to=b'media/media/dist/', null=True, verbose_name=b'Miniaturka', blank=True),
        ),
    ]
