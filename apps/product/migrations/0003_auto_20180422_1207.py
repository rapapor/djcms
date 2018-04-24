# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('product', '0002_logisticdata_logistic_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=cms.models.fields.PlaceholderField(related_name='product_content_en', slotname=b'content_en', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_pl',
            field=cms.models.fields.PlaceholderField(related_name='product_content_pl', slotname=b'content_pl', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='best_seller',
            field=models.BooleanField(default=False, help_text='Zaznacz je\u017celi produkt ma by\u0107 bestsellerem', verbose_name=b'Bestseller Tak/Nie'),
        ),
        migrations.AlterField(
            model_name='product',
            name='best_seller_file',
            field=models.ImageField(upload_to=b'media/media/bestSellerMini/', null=True, verbose_name=b'Miniaturka Bestsellera 322x307px', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file_1',
            field=models.ImageField(upload_to=b'media/media/produkt_img/', null=True, verbose_name=b'Produkt zdjecie 1 ', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file_2',
            field=models.ImageField(upload_to=b'media/media/produkt_img/', null=True, verbose_name=b'Produkt zdjecie 2 ', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file_3',
            field=models.ImageField(upload_to=b'media/media/produkt_img/', null=True, verbose_name=b'Produkt zdjecie 3 ', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_mini_file',
            field=models.ImageField(upload_to=b'media/media/produkt_mini/', null=True, verbose_name=b'Miniaturka 370x278px', blank=True),
        ),
    ]
