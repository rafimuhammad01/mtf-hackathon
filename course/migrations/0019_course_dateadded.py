# Generated by Django 3.2 on 2021-05-05 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20210501_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 5, 14, 10, 10, 682036)),
        ),
    ]
