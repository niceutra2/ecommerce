# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-10 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170709_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]