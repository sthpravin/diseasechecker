# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-25 04:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0008_auto_20170725_0409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='Specialization',
            new_name='specialization',
        ),
    ]