# Generated by Django 4.2.5 on 2023-09-04 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_student_code_parainage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='generated_code',
        ),
    ]