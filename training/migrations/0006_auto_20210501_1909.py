# Generated by Django 3.2 on 2021-05-01 12:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_alter_schedule_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='training',
            name='organizer',
            field=models.CharField(default='MTF', max_length=50),
            preserve_default=False,
        ),
    ]
