# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventoj', '0005_auto_20140525_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='kioma',
            field=models.CharField(default='', help_text='42-a', max_length=10, verbose_name='kioma', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='arangxo',
            name='dauro',
            field=models.PositiveIntegerField(help_text=b'Gxenerala dauxro de la renkontigxo, en tagoj.', null=True, verbose_name='dauxro', blank=True),
        ),
        migrations.AlterField(
            model_name='arangxo',
            name='facebook',
            field=models.CharField(help_text=b'https://www.facebook.com/[...]', max_length=255, verbose_name='facebook identigilo', blank=True),
        ),
        migrations.AlterField(
            model_name='arangxo',
            name='nomo',
            field=models.CharField(help_text='gxenerala nomo de la arangxo, sen numero aux dato', unique=True, max_length=255, verbose_name='nomo de la renkontigxo'),
        ),
        migrations.AlterField(
            model_name='arangxo',
            name='twitter',
            field=models.CharField(help_text=b'https://twitter.com/[...]', max_length=255, verbose_name='twitter identigilo', blank=True),
        ),
    ]
