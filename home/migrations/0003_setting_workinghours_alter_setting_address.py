# Generated by Django 4.0.5 on 2022-06-25 10:01

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='workinghours',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=100),
        ),
    ]
