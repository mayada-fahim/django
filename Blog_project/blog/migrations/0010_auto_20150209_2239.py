# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150209_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('user_name', models.CharField(max_length=100, unique=True, serialize=False, primary_key=True)),
                ('user_password', models.CharField(max_length=100)),
                ('user_mail', models.EmailField(unique=True, max_length=75)),
                ('user_status', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
