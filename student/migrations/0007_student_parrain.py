# Generated by Django 4.2.5 on 2023-09-04 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_student_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parrain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student'),
        ),
    ]