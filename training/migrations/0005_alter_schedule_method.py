# Generated by Django 3.2 on 2021-05-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_auto_20210501_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='method',
            field=models.IntegerField(blank=True, choices=[(0, 'Online'), (1, 'Offline')], null=True),
        ),
    ]