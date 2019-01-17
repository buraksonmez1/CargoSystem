# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-01-01 15:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'The username is already exist.'}, max_length=255, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-Mail Address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last Name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Joined')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user account should be considered active. Set this flag to False instead of deleting accounts.', verbose_name='Active Status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether this user can access the admin site.', verbose_name='Staff Status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Super User Status')),
                ('user_type', models.CharField(choices=[('manager', 'Manager'), ('transporter', 'Transporter'), ('customer', 'Customer')], default='customer', max_length=50, verbose_name='User Type')),
                ('tc_no', models.IntegerField(blank=True, error_messages={'unique': 'The username is already exist.'}, null=True, unique=True, verbose_name='TC NO')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
        migrations.CreateModel(
            name='IsikCargos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_who', models.CharField(max_length=255)),
                ('created_cargo_date', models.DateTimeField(auto_now_add=True)),
                ('taken_cargo_date', models.DateField(blank=True, null=True)),
                ('to_who', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('who_has_now', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
