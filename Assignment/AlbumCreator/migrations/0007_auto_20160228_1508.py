# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlbumCreator', '0006_auto_20160228_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='url_name',
            field=models.CharField(max_length=200),
        ),
    ]
