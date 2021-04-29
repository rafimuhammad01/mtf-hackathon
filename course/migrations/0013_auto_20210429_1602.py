# Generated by Django 3.2 on 2021-04-29 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20210429_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='nextID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idNext', to='course.step'),
        ),
        migrations.AddField(
            model_name='step',
            name='prevID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='idPrev', to='course.step'),
        ),
    ]
