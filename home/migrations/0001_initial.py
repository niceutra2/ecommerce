# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-16 04:41
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import home.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='email')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='name')),
                ('date_of_birth', models.DateTimeField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('address', models.CharField(blank=True, help_text='주소를 입력하세요', max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=home.models.get_upload_path, verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='상품명', max_length=50, verbose_name='TITLE')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('price', models.IntegerField(default=0, help_text='가격')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('discount_percent', models.IntegerField(help_text='할인률')),
                ('rating', models.IntegerField(default=0, help_text='평점')),
                ('choice_field', models.CharField(choices=[('Discount', 'Discount'), ('Sale', 'Sale'), ('TimeSale', 'TimeSale'), ('Normal', 'Normal')], max_length=10)),
            ],
            options={
                'ordering': ('-create_date',),
                'verbose_name_plural': 'products',
                'verbose_name': 'product',
                'db_table': 'all_products',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_size', models.IntegerField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Product'),
        ),
    ]
