# Generated by Django 3.0.8 on 2020-08-08 20:07

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]