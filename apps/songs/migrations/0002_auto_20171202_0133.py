# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-02 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='author',
            new_name='link',
        ),
    ]
