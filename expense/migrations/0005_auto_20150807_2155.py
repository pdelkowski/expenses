# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20150806_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseitem',
            name='category',
            field=models.ForeignKey(related_query_name=b'item', related_name='items', blank=True, to='expense.ExpenseCategory', null=True),
        ),
        migrations.AlterField(
            model_name='expenseitem',
            name='cost',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='expenseitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 19, 55, 1, 958013, tzinfo=utc)),
        ),
    ]
