# Generated by Django 4.0.5 on 2022-06-23 20:38

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_category_image_alter_images_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255),
        ),
    ]