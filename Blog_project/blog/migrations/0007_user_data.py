# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150210_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=100)),
                ('user_password', models.CharField(max_length=100)),
                ('user_mail', models.EmailField(unique=True, max_length=75)),
                ('user_status', models.BooleanField(default=False)),
            ],
        ),
    ]
