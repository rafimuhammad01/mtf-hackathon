# Generated by Django 3.2 on 2021-04-28 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210428_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionowned',
            name='lessonOwned',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.lessonowned'),
        ),
    ]