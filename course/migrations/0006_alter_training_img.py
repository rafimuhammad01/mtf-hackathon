# Generated by Django 3.2 on 2021-04-28 11:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
