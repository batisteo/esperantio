# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventoj', '0004_arangxo_ligila_nomo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arangxo',
            old_name='ligila_nomo',
            new_name='slug',
        ),
    ]
