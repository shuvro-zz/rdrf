# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0024_patient_patient_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={
                'ordering': [
                    'family_name',
                    'given_names',
                    'date_of_birth'],
                'permissions': (
                    ('can_see_full_name',
                     'Can see Full Name column'),
                    ('can_see_dob',
                     'Can see Date of Birth column'),
                    ('can_see_working_groups',
                     'Can see Working Groups column'),
                    ('can_see_diagnosis_progress',
                     'Can see Diagnosis Progress column'),
                    ('can_see_diagnosis_currency',
                     'Can see Diagnosis Currency column'),
                    ('can_see_genetic_data_map',
                     'Can see Genetic Module column'),
                    ('can_see_data_modules',
                     'Can see Data Modules column'),
                    ('can_see_code_field',
                     'Can see Code Field column')),
                'verbose_name_plural': 'Patient List'},
        ),
    ]
