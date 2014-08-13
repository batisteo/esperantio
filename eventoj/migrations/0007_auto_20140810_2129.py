# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventoj', '0006_auto_20140808_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arangxo',
            name='nomo',
            field=models.CharField(unique=True, max_length=255, verbose_name='nomo de la renkontigxo'),
        ),
    ]
