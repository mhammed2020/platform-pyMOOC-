# Generated by Django 3.2 on 2021-04-30 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0004_course_duree'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
