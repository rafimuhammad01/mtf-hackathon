# Generated by Django 3.2 on 2021-04-28 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='type',
            field=models.IntegerField(choices=[(0, 'Lesson'), (1, 'Quiz')]),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlightText', models.TextField(max_length=255)),
                ('notes', models.TextField(max_length=255)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='courseowned',
            name='notes',
            field=models.ManyToManyField(blank=True, to='course.Notes'),
        ),
    ]
