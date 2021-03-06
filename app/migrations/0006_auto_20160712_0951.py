# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 01:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160630_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=40, verbose_name=b'HOST')),
                ('path', models.CharField(default=b'/', max_length=100, verbose_name=b'FILE')),
                ('isPost', models.IntegerField(max_length=1, verbose_name=b'isPost')),
                ('postData', models.TextField(verbose_name=b'postData')),
                ('filetype', models.CharField(max_length=40, verbose_name=b'filetype')),
                ('isComplete', models.IntegerField(max_length=1, verbose_name=b'isPost')),
                ('queryed', models.IntegerField(default=0, max_length=1, verbose_name=b'isPost')),
            ],
            options={
                'db_table': 'burp',
            },
        ),
        migrations.CreateModel(
            name='Burpk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default=b'', max_length=40, verbose_name=b'HOST')),
                ('p_hash', models.CharField(default=b'', max_length=100, verbose_name=b'p_hash')),
                ('p_id', models.IntegerField(default=0, verbose_name=b'p_id')),
            ],
            options={
                'db_table': 'burpk',
            },
        ),
        migrations.AlterField(
            model_name='icpcheck',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 9, 51, 39, 135441), null=True),
        ),
        migrations.AlterField(
            model_name='subdomainbrute',
            name='fuzz_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 9, 51, 39, 135991), null=True),
        ),
    ]
