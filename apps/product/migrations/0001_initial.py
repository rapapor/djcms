# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogisticData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name_pl', models.CharField(max_length=50, null=True, verbose_name=b'Nazwa PL', blank=True)),
                ('product_name_en', models.CharField(max_length=50, null=True, verbose_name=b'Nazwa EN', blank=True)),
                ('form_pl', models.CharField(max_length=50, null=True, verbose_name=b'Forma PL', blank=True)),
                ('form_en', models.CharField(max_length=50, null=True, verbose_name=b'Forma EN', blank=True)),
                ('single_pack_pl', models.CharField(max_length=50, null=True, verbose_name=b'Opakowanie jedn. PL', blank=True)),
                ('single_pack_en', models.CharField(max_length=50, null=True, verbose_name=b'Opakowanie jedn. EN', blank=True)),
                ('multi_pack_pl', models.CharField(max_length=50, null=True, verbose_name=b'Paletyzacja PL', blank=True)),
                ('multi_pack_en', models.CharField(max_length=50, null=True, verbose_name=b'Paletyzacja EN', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('best_seller', models.BooleanField(default=False, verbose_name=b'Czy produkt jest BestSellerem')),
                ('best_seller_file', models.ImageField(upload_to=b'media/bestSellerMini/', null=True, verbose_name=b'Miniaturka Bestsellera 322x307px', blank=True)),
                ('product_mini_file', models.ImageField(upload_to=b'media/produkt_mini/', null=True, verbose_name=b'Miniaturka 370x278px', blank=True)),
                ('name_pl', models.CharField(max_length=50, verbose_name=b'Nazwa PL')),
                ('name_en', models.CharField(max_length=50, verbose_name=b'Nazwa EN')),
                ('desc_mini_pl', models.CharField(max_length=150, verbose_name=b'Zajawka PL')),
                ('desc_mini_en', models.CharField(max_length=150, verbose_name=b'Zajawka EN')),
                ('category', models.CharField(default=b'gastro', max_length=25, choices=[(b'gastro', b'Gastronomia'), (b'biz', b'Biznes')])),
                ('desc_pl', models.TextField(verbose_name=b'Opis PL')),
                ('desc_en', models.TextField(verbose_name=b'Opis EN')),
                ('product_file_1', models.ImageField(upload_to=b'media/produkt_img/', null=True, verbose_name=b'Produkt zdjecie 1 ', blank=True)),
                ('product_file_2', models.ImageField(upload_to=b'media/produkt_img/', null=True, verbose_name=b'Produkt zdjecie 2 ', blank=True)),
                ('product_file_3', models.ImageField(upload_to=b'media/produkt_img/', null=True, verbose_name=b'Produkt zdjecie 3 ', blank=True)),
                ('pizza_pl', models.TextField(null=True, verbose_name=b'Piec do pizzy PL', blank=True)),
                ('pizza_en', models.TextField(null=True, verbose_name=b'Piec do pizzy EN', blank=True)),
                ('bake_kon_pl', models.TextField(null=True, verbose_name=b'Piec konwekcyjny PL', blank=True)),
                ('bake_kon_en', models.TextField(null=True, verbose_name=b'Piec konwekcyjny EN', blank=True)),
                ('mikrofave_pl', models.TextField(null=True, verbose_name=b'Mikrofala PL', blank=True)),
                ('mikrofave_en', models.TextField(null=True, verbose_name=b'Mikrofala EN', blank=True)),
                ('pan_pl', models.TextField(null=True, verbose_name=b'Patelnia PL', blank=True)),
                ('pan_en', models.TextField(null=True, verbose_name=b'Patelnia EN', blank=True)),
                ('pot_pl', models.TextField(null=True, verbose_name=b'Garnek PL', blank=True)),
                ('pot_en', models.TextField(null=True, verbose_name=b'Garnek EN', blank=True)),
                ('bake_pl', models.TextField(null=True, verbose_name=b'Piekarnik PL', blank=True)),
                ('bake_en', models.TextField(null=True, verbose_name=b'Piekarnik EN', blank=True)),
                ('toaster_op_pl', models.TextField(null=True, verbose_name=b'Opiekacz PL', blank=True)),
                ('toaster_op_en', models.TextField(null=True, verbose_name=b'Opiekacz EN', blank=True)),
                ('grill_pl', models.TextField(null=True, verbose_name=b'Grill PL', blank=True)),
                ('grill_en', models.TextField(null=True, verbose_name=b'Grill EN', blank=True)),
                ('toster_pl', models.TextField(null=True, verbose_name=b'Toster  PL', blank=True)),
                ('toster_en', models.TextField(null=True, verbose_name=b'Toster  PL', blank=True)),
                ('slug', models.SlugField(default=b'')),
            ],
        ),
    ]
