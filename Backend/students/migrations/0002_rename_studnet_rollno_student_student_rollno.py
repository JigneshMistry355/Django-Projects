# Generated by Django 4.2.7 on 2024-03-07 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studnet_rollno',
            new_name='student_rollno',
        ),
    ]
