# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20180503_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bake_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bake_kon_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bake_kon_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='bake_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='grill_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='grill_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mikrofave_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mikrofave_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pan_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pan_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pizza_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pizza_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pot_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pot_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toaster_op_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toaster_op_pl',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toster_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='toster_pl',
        ),
    ]
