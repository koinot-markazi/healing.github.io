# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-20 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180520_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.CharField(help_text='Вводите тэги через пробел', max_length=511),
        ),
    ]
