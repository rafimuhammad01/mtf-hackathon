# Generated by Django 3.2 on 2021-04-27 18:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('JWTAuth', '0001_initial'),
        ('forum', '0007_auto_20210428_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50)),
                ('isRight', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('img', models.ImageField(blank=True, max_length=255, null=True, upload_to='img/%Y/%m/%d/')),
                ('price', models.FloatField(default=0)),
                ('reward', models.FloatField(default=0)),
                ('about', ckeditor.fields.RichTextField(blank=True)),
                ('learningPoint', ckeditor.fields.RichTextField(blank=True)),
                ('rating', models.FloatField(default=0)),
                ('estimateTime', models.TimeField(default=0)),
                ('forum', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LessonOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isComplete', models.BooleanField(default=False)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('point', models.FloatField(default=0.0)),
                ('choice1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice1', to='course.choice')),
                ('choice2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice2', to='course.choice')),
                ('choice3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice3', to='course.choice')),
                ('choice4', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='choice4', to='course.choice')),
            ],
        ),
        migrations.CreateModel(
            name='QuizOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRight', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(0, 'Staff'), (1, 'Admin')])),
                ('description', models.TextField(blank=True, max_length=255)),
                ('minimumQuizScore', models.FloatField(default=0)),
                ('lesson', models.ManyToManyField(blank=True, to='course.Lesson')),
                ('quiz', models.ManyToManyField(blank=True, to='course.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(0, 'Text'), (1, 'Video')])),
                ('contentText', ckeditor.fields.RichTextField(blank=True)),
                ('contentVideo', models.URLField(blank=True)),
                ('transcript', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, max_length=255, null=True, upload_to='img/%Y/%m/%d/')),
                ('schedule', models.ManyToManyField(blank=True, to='course.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.training')),
            ],
        ),
        migrations.CreateModel(
            name='StepOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeConsume', models.TimeField(default=0)),
                ('isComplete', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.step')),
            ],
        ),
        migrations.CreateModel(
            name='SectionOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizResult', models.FloatField(blank=True, default=0.0)),
                ('isComplete', models.BooleanField(default=False)),
                ('isPassedQuiz', models.BooleanField(default=False)),
                ('lessonOwned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lessonowned')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
                ('quizOwned', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.quizowned')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section')),
            ],
        ),
        migrations.AddField(
            model_name='lessonowned',
            name='stepOwned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.stepowned'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='step',
            field=models.ManyToManyField(blank=True, to='course.Step'),
        ),
        migrations.CreateModel(
            name='CourseOwned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField(default=0.0)),
                ('isComplete', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('lastLesson', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.lesson')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
                ('sectionOwned', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='course.sectionowned')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='section',
            field=models.ManyToManyField(to='course.Section'),
        ),
        migrations.AddField(
            model_name='course',
            name='topic',
            field=models.ManyToManyField(blank=True, to='forum.Topic'),
        ),
    ]
