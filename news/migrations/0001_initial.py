# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_blank', models.BooleanField(default=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('resend_request', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(max_length=20)),
                ('section_id', models.IntegerField()),
                ('thumbnail', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image_source', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
                ('share_url', models.CharField(blank=True, max_length=100, null=True)),
                ('ga_prefix', models.CharField(blank=True, max_length=36, null=True)),
                ('date', models.DateField()),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('type', models.IntegerField(default=0)),
                ('story_id', models.IntegerField()),
                ('cover_images', models.TextField(blank=True, null=True)),
                ('js', models.TextField(blank=True, null=True)),
                ('css', models.TextField(blank=True, null=True)),
                ('recommenders', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=20)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Section')),
            ],
        ),
    ]