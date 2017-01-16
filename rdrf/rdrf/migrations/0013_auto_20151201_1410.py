# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdrf', '0012_registryform_header'),
    ]

    operations = [migrations.AlterField(model_name='emailtemplate', name='language', field=models.CharField(
        max_length=2, choices=[('ar', 'Arabic'), ('de', 'German'), ('en', 'English'), ('no', 'Norwegian')]), ), ]
