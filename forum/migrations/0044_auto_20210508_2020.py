# Generated by Django 3.2 on 2021-05-08 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0043_auto_20210506_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 20, 20, 9, 197305)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 20, 20, 9, 193317)),
        ),
    ]