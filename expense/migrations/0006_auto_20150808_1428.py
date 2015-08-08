# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0005_auto_20150807_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
