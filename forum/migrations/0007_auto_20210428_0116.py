# Generated by Django 3.2 on 2021-04-27 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20210428_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 1, 16, 38, 226423)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 1, 16, 38, 222376)),
        ),
    ]
