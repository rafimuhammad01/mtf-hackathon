# Generated by Django 3.2 on 2021-05-08 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0025_auto_20210506_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstime',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 20, 20, 9, 271107)),
        ),
        migrations.AlterField(
            model_name='course',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 20, 20, 9, 257147)),
        ),
        migrations.AlterField(
            model_name='courseowned',
            name='dateJoined',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 20, 20, 9, 267120)),
        ),
    ]
