# Generated by Django 3.2 on 2021-05-06 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_auto_20210506_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourseaccess',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 10, 43, 37, 686476)),
        ),
        migrations.AlterField(
            model_name='course',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 10, 43, 37, 671484)),
        ),
    ]
