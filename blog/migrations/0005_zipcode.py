# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160728_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zipcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=6)),
            ],
            options={
                'ordering': ['zipcode'],
            },
        ),
    ]
