# Generated by Django 3.2 on 2021-05-05 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20210506_0025'),
        ('forum', '0041_auto_20210501_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_owner', to='course.course'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 0, 25, 2, 922084)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 6, 0, 25, 2, 918645)),
        ),
    ]
