# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidr', models.CharField(max_length=39, verbose_name='CIDR')),
                ('ip_first', models.GenericIPAddressField(verbose_name='First IP')),
                ('ip_last', models.GenericIPAddressField(verbose_name='Last IP')),
                ('organization', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=200)),
            ],
        ),
    ]