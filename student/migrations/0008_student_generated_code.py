# Generated by Django 4.2.5 on 2023-09-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_student_parrain'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='generated_code',
            field=models.BooleanField(default=False),
        ),
    ]