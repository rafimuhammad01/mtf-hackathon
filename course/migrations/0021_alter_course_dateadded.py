# Generated by Django 3.2 on 2021-05-05 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20210506_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 0, 25, 30, 534146)),
        ),
    ]
