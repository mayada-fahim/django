# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=250)),
                ('comment_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_text', models.CharField(max_length=2000)),
                ('post_date', models.DateTimeField(verbose_name=b'date published')),
                ('post_image', models.ImageField(default=b'null', upload_to=b'static/images/article')),
                ('post_like', models.IntegerField(default=0)),
                ('published', models.BooleanField(default=False)),
                ('post_title', models.CharField(default=b'', max_length=50)),
            ],
        ),
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
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(default=1, to='blog.Post'),
        ),
    ]
