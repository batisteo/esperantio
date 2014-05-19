# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventoj', '0002_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='arangxo',
            name='facebook',
            field=models.CharField(default='', max_length=255, verbose_name='facebook', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arangxo',
            name='min_homoj',
            field=models.PositiveIntegerField(default=0, verbose_name='minimuma nombro da partoprenantoj'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arangxo',
            name='twitter',
            field=models.CharField(default='', max_length=255, verbose_name='twitter', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arangxo',
            name='max_homoj',
            field=models.PositiveIntegerField(default=0, verbose_name='maksimuma nombro da partoprenantoj'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='evento',
            name='nb_partoprenantoj',
        ),
        migrations.RemoveField(
            model_name='arangxo',
            name='nb_partoprenantoj',
        ),
    ]
