# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('addr', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('contact', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Name_ID',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='nam',
            field=models.ForeignKey(to='FIRSTAPPLICATION.Name_ID'),
        ),
        migrations.AddField(
            model_name='address',
            name='con',
            field=models.ForeignKey(to='FIRSTAPPLICATION.Contact'),
        ),
    ]
