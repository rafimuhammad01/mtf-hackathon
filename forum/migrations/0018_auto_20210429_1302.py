# Generated by Django 3.2 on 2021-04-29 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_auto_20210429_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 13, 2, 19, 321798)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 13, 2, 19, 318769)),
        ),
    ]
