# Generated by Django 4.2.5 on 2023-09-04 14:33

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
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('sold', models.BooleanField(default=False)),
                ('num_of_pic', models.PositiveIntegerField(default=0)),
                ('code_parainage', models.CharField(blank=True, max_length=6, unique=True)),
            ],
        ),
    ]
