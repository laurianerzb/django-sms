# Generated by Django 3.0.7 on 2024-08-14 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_duration',
            field=models.CharField(default='1 month', max_length=100),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_lecturer',
            field=models.CharField(default='Admin', max_length=255),
        ),
    ]
