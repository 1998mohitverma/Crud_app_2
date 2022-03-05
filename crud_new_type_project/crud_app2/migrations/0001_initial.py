# Generated by Django 3.0 on 2021-09-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('contact', models.CharField(max_length=10)),
                ('department', models.CharField(max_length=70)),
                ('emp_id', models.CharField(max_length=5)),
                ('password', models.CharField(max_length=70)),
            ],
        ),
    ]
