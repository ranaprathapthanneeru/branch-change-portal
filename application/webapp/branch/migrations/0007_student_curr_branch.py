# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_auto_20151027_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='curr_branch',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
