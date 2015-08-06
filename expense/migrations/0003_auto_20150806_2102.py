# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_expenseitem_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensecategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='expenseitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
