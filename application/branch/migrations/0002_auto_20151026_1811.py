# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchchange',
            name='cpi',
            field=models.FloatField(),
        ),
    ]
