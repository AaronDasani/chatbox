# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-01 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poke_count', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poke_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked_from_user', to='users.User')),
                ('poke_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poked_user', to='users.User')),
            ],
        ),
    ]
