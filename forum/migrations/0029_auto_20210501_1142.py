# Generated by Django 3.2 on 2021-05-01 04:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0028_auto_20210501_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 11, 42, 3, 688227)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 1, 11, 42, 3, 685235)),
        ),
    ]
