# Generated by Django 3.2.3 on 2021-05-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0002_student_prenume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nume',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='prenume',
            field=models.CharField(max_length=20),
        ),
    ]
