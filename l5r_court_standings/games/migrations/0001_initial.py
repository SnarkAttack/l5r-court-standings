# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.IntegerField(blank=True, null=True)),
                ('player2', models.IntegerField(blank=True, null=True)),
                ('player1_clan', models.IntegerField(blank=True, null=True)),
                ('player2_clan', models.IntegerField(blank=True, null=True)),
                ('player1_splash', models.IntegerField(blank=True, null=True)),
                ('player2_splash', models.IntegerField(blank=True, null=True)),
                ('winner', models.BooleanField()),
                ('win_type', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('screen_name', models.CharField(max_length=32)),
            ],
        ),
    ]
