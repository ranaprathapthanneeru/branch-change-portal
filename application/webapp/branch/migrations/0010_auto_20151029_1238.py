# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0009_student_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(max_length=6),
        ),
    ]
