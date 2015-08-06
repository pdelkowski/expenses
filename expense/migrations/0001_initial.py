# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default=b'No description', blank=True)),
                ('created_at', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.ForeignKey(to='expense.ExpenseCategory')),
            ],
        ),
    ]
