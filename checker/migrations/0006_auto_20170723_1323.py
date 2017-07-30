# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-23 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0005_patient_possible_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='disease_description',
            field=models.CharField(default='NA', max_length=500),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_ref',
            field=models.URLField(default='NA'),
        ),
    ]