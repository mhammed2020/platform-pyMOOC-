# Generated by Django 3.2 on 2021-05-10 10:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0006_alter_course_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-post_date',)},
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
