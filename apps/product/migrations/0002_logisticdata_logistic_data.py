# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logisticdata',
            name='Logistic_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', to='product.Product', max_length=60, help_text='Wybierz dane logistyczne dla produktu', null=True),
        ),
    ]
