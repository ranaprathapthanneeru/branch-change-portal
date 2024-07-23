# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0010_auto_20151029_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchchange',
            name='category',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='branchchange',
            name='current_branch',
            field=models.CharField(max_length=100),
        ),
    ]
