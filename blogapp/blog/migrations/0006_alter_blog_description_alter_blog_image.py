# Generated by Django 4.2.4 on 2023-08-20 23:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
