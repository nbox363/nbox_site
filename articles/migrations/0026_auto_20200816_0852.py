# Generated by Django 3.1 on 2020-08-16 08:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20200814_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
