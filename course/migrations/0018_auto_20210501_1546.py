# Generated by Django 3.2 on 2021-05-01 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JWTAuth', '0001_initial'),
        ('course', '0017_auto_20210501_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('minimumQuizScore', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuizSectionOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isComplete', models.BooleanField(default=False)),
                ('quizResult', models.FloatField(blank=True, default=0.0)),
                ('isPassedQuiz', models.BooleanField(default=False)),
                ('attempt', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
                ('quizOwned', models.ManyToManyField(blank=True, null=True, to='course.QuizOwned')),
                ('quizSection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.quizsection')),
            ],
        ),
        migrations.RemoveField(
            model_name='training',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='trainingowned',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='trainingowned',
            name='training',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='title',
        ),
        migrations.RemoveField(
            model_name='section',
            name='minimumQuizScore',
        ),
        migrations.RemoveField(
            model_name='section',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='sectionowned',
            name='isPassedQuiz',
        ),
        migrations.RemoveField(
            model_name='sectionowned',
            name='quizOwned',
        ),
        migrations.RemoveField(
            model_name='sectionowned',
            name='quizResult',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.DeleteModel(
            name='TrainingOwned',
        ),
        migrations.AddField(
            model_name='quizsection',
            name='quiz',
            field=models.ManyToManyField(to='course.Quiz'),
        ),
        migrations.AddField(
            model_name='section',
            name='quizSection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.quizsection'),
        ),
        migrations.AddField(
            model_name='sectionowned',
            name='quizSectionOwned',
            field=models.ManyToManyField(blank=True, to='course.QuizSectionOwned'),
        ),
        migrations.AlterField(
            model_name='courseowned',
            name='lastQuiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.quizsection'),
        ),
    ]
