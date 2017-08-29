# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-21 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170820_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='size',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]