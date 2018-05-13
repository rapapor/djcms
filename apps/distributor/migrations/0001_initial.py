# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20180503_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, help_text='Zaznacz jezeli chcesz wyswietlic dystrybutora', verbose_name=b'Aktywny Tak/Nie')),
                ('biz_name_pl', models.CharField(max_length=200, verbose_name=b'Nazwa firmy PL')),
                ('biz_name_en', models.CharField(max_length=200, verbose_name=b'Nazwa firmy EN')),
                ('woj_pl', models.CharField(max_length=200, verbose_name=b'wojewodztwo PL')),
                ('woj_en', models.CharField(max_length=200, verbose_name=b'wojewodztwo EN')),
                ('street_pl', models.CharField(max_length=200, verbose_name=b'ulica i kod pocztowy PL')),
                ('street_en', models.CharField(max_length=200, verbose_name=b'ulica i kod pocztowy EN')),
                ('phone', models.CharField(max_length=200, verbose_name=b'telefon')),
                ('gmapCoordynator_x', models.CharField(max_length=200, verbose_name=b'koordynaty google map x')),
                ('gmapCoordynator_y', models.CharField(max_length=200, verbose_name=b'koordynaty google map y')),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
        ),
    ]
