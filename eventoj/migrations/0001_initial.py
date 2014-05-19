# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.models
import django.utils.timezone
from django.conf import settings
import taggit.managers
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '__first__'),
        ('organizoj', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arangxo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('kreanto', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', verbose_name='Kreanto')),
                ('nomo', models.CharField(unique=True, max_length=255, verbose_name='nomo de la renkontigxo')),
                ('mallonga_nomo', models.CharField(help_text='Mallonga nomo se ekzistas.', max_length=255, verbose_name='mallonga nomo', blank=True)),
                ('retejo', models.URLField(verbose_name='retejo', blank=True)),
                ('retposxto', models.EmailField(max_length=75, verbose_name='retposxto', blank=True)),
                ('organizo', models.ForeignKey(verbose_name='organizo', to_field='id', blank=True, to='organizoj.Organizo', null=True)),
                ('publiko', models.PositiveSmallIntegerField(default=0, max_length=1, null=True, verbose_name='publiko', choices=[(0, 'cxiuj'), (1, 'plenkreskuloj'), (2, 'familioj'), (3, 'junuloj'), (4, 'infanoj')])),
                ('nb_partoprenantoj', models.PositiveIntegerField(help_text=b'Proksimuma nombro da partoprenantoj.', verbose_name='nombro da partoprenantoj')),
                ('ofteco', models.PositiveIntegerField(blank=True, help_text=b'Gxenerala ofteco de la renkontigxo.', null=True, verbose_name='ofteco', choices=[(0, 'malregule'), (1, 'tage'), (2, 'dutage'), (4, 'foje semajne'), (7, 'semajne'), (14, 'dusemajne'), (30, 'monate'), (61, 'dumonate'), (183, 'sesmonate'), (365, 'jare'), (999, 'malofte')])),
                ('dauro', models.PositiveIntegerField(help_text=b'Gxenerala dauxro de la renkontigxo.', null=True, verbose_name='dauxro', blank=True)),
                ('etikedoj', taggit.managers.TaggableManager(to=taggit.models.Tag, through=taggit.models.TaggedItem, blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'arangxo',
                'verbose_name_plural': 'arangxoj',
            },
            bases=(models.Model,),
        ),
    ]
