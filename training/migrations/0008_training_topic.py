# Generated by Django 3.2 on 2021-05-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0043_auto_20210506_0219'),
        ('training', '0007_auto_20210501_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='topic',
            field=models.ManyToManyField(blank=True, to='forum.Topic'),
        ),
    ]
