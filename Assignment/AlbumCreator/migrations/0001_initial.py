# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('album_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=200, unique=True)),
                ('owner', models.CharField(max_length=200)),
                ('like_total', models.IntegerField(blank=True)),
                ('photo_location', models.ImageField(upload_to='/photos/')),
                ('stored_date', models.DateTimeField(blank=True)),
                ('slug_owner_name', models.SlugField(blank=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Photos', to='AlbumCreator.Album')),
            ],
        ),
    ]
