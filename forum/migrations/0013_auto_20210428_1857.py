# Generated by Django 3.2 on 2021-04-28 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20210428_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 18, 57, 49, 739621)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 18, 57, 49, 736632)),
        ),
    ]