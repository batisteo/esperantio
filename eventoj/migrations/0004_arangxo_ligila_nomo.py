# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eventoj', '0003_auto_20140519_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='arangxo',
            name='ligila_nomo',
            field=autoslug.fields.AutoSlugField(default='', editable=False, unique=True, verbose_name='ligila nomo'),
            preserve_default=False,
        ),
    ]
