# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_pl', models.CharField(max_length=200, verbose_name=b'Tytul PL')),
                ('title_en', models.CharField(max_length=200, verbose_name=b'Tytul EN')),
                ('pub_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'data publikacji')),
                ('content_pl', models.TextField(verbose_name=b'Tresc PL')),
                ('content_en', models.TextField(verbose_name=b'Tresc EN')),
                ('tip_pl', models.CharField(max_length=200, verbose_name=b'tekst zachety PL')),
                ('tip_en', models.CharField(max_length=200, verbose_name=b'tekst zachety EN')),
                ('image', models.ImageField(null=True, upload_to=b'media/', blank=True)),
            ],
        ),
    ]
