# Generated by Django 3.2 on 2021-05-04 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('JWTAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=50)),
                ('balance', models.FloatField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JWTAuth.employee')),
            ],
        ),
    ]
