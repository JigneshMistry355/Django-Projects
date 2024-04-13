# Generated by Django 4.2.7 on 2024-03-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studnet_rollno', models.IntegerField(unique=True)),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_city', models.CharField(max_length=50)),
                ('student_percentage', models.FloatField()),
            ],
        ),
    ]