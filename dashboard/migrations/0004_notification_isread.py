# Generated by Django 3.2 on 2021-05-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_notification_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
    ]
