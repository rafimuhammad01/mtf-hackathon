# Generated by Django 3.2 on 2021-04-23 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20210423_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 23, 16, 42, 26, 851017)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
