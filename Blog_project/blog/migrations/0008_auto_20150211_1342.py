# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_user_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='id',
        ),
        migrations.AddField(
            model_name='user_data',
            name='user_image',
            field=models.ImageField(default=b'null', upload_to=b'static/user_images'),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='user_name',
            field=models.CharField(max_length=100, unique=True, serialize=False, primary_key=True),
        ),
    ]
