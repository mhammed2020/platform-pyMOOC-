# Generated by Django 3.2 on 2021-05-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0002_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
