# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, help_text='Zaznacz jezeli chcesz wyswietlic kontakt', verbose_name=b'Aktywny Tak/Nie')),
                ('name_pl', models.CharField(max_length=200, verbose_name=b'Imie Nazwisko PL')),
                ('name_en', models.CharField(max_length=200, verbose_name=b'Imie Nazwisko EN')),
                ('position_pl', models.CharField(max_length=200, verbose_name=b'Stanowisko PL')),
                ('position_en', models.CharField(max_length=200, verbose_name=b'Stanowisko EN')),
                ('email', models.CharField(max_length=200, verbose_name=b'email')),
                ('phone', models.CharField(max_length=200, verbose_name=b'telefon')),
                ('section', models.CharField(default=b'SELLER', max_length=20, choices=[(b'SELLER', b'seller'), (b'BUYER', b'buyer'), (b'PRODUCTION', b'production'), (b'HR', b'hr')])),
                ('contact_file', models.ImageField(upload_to=b'media/media/contact/', null=True, verbose_name=b'Miniaturka', blank=True)),
            ],
        ),
    ]
