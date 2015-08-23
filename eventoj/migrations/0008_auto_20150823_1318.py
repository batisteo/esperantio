# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventoj', '0007_auto_20140810_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='posxtkodo',
            field=models.CharField(max_length=30, verbose_name='posxtkodo', blank=True),
            preserve_default=True,
        ),
    ]
