# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseitem',
            name='cost',
            field=models.IntegerField(default=0),
        ),
    ]
