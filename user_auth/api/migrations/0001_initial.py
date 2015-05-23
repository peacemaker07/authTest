# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('summary', models.CharField(max_length=128, verbose_name='タスク')),
                ('complete', models.BooleanField(verbose_name='状態', default=False)),
                ('comment', models.CharField(blank=True, max_length=512, verbose_name='コメント')),
                ('done_date', models.DateField(blank=True, verbose_name='完了日', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='tasks')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
