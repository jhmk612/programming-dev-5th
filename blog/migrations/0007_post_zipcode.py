# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 02:09
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='zipcode',
            field=models.CharField(default='06267', help_text='우편번호를 입력', max_length=10, validators=[blog.models.zipcode_validator]),
            preserve_default=False,
        ),
    ]
