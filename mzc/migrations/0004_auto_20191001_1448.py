# Generated by Django 2.1.3 on 2019-10-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mzc', '0003_students_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(max_length=30, null='TRUE'),
        ),
    ]
