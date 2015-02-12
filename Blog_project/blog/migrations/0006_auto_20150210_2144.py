# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150210_2140'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user_data',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_date',
        ),
    ]
