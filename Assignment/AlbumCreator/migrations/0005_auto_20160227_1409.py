# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlbumCreator', '0004_auto_20160227_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_location',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]