# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_auto_20150806_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseitem',
            name='category',
            field=models.ForeignKey(blank=True, to='expense.ExpenseCategory', null=True),
        ),
    ]
