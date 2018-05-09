# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False, help_text='Zaznacz jezeli chcesz opublikowac ogloszenie', verbose_name=b'Aktywne Tak/Nie')),
                ('pub_date', models.DateField(default=django.utils.timezone.now, verbose_name=b'data publikacji')),
                ('position_pl', models.CharField(max_length=200, verbose_name=b'stanowisko PL')),
                ('position_en', models.CharField(max_length=200, verbose_name=b'stanowisko EN')),
                ('city', models.CharField(max_length=200, verbose_name=b'Miasto')),
                ('slug', models.SlugField(default=b'')),
                ('content_en', cms.models.fields.PlaceholderField(related_name='job_offer_EN', slotname=b'content_en', editable=False, to='cms.Placeholder', null=True)),
                ('content_pl', cms.models.fields.PlaceholderField(related_name='job_offer_PL', slotname=b'content_pl', editable=False, to='cms.Placeholder', null=True)),
            ],
        ),
    ]
