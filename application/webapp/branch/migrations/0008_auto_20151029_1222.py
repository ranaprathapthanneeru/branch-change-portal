# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0007_student_curr_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='curr_branch',
            field=models.CharField(max_length=8),
        ),
    ]
