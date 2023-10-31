# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0008_auto_20151029_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='category',
            field=models.CharField(max_length=6, blank=True),
        ),
    ]
