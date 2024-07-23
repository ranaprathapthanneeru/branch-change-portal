# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchChange',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=400)),
                ('current_branch', models.CharField(max_length=3, choices=[('EE', 'ElectricalEngeenering'), ('CS', 'ComputerScienceEngenering'), ('ME', 'MechanicalEngeneering')])),
                ('cpi', models.IntegerField()),
                ('category', models.CharField(max_length=3, choices=[('GE', 'GE'), ('SC', 'SC'), ('OBC', 'OBC')])),
                ('preference1', models.CharField(max_length=3, choices=[('EE', 'ElectricalEngeenering'), ('CS', 'ComputerScienceEngenering'), ('ME', 'MechanicalEngeneering')])),
                ('preference2', models.CharField(max_length=3, choices=[('EE', 'ElectricalEngeenering'), ('CS', 'ComputerScienceEngenering'), ('ME', 'MechanicalEngeneering')])),
                ('preference3', models.CharField(max_length=3, choices=[('EE', 'ElectricalEngeenering'), ('CS', 'ComputerScienceEngenering'), ('ME', 'MechanicalEngeneering')])),
                ('preference4', models.CharField(max_length=3, choices=[('EE', 'ElectricalEngeenering'), ('CS', 'ComputerScienceEngenering'), ('ME', 'MechanicalEngeneering')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=400, blank=True)),
                ('cpi', models.FloatField()),
            ],
        ),
    ]
