# Generated by Django 3.1 on 2020-08-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20200813_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(max_length=120, verbose_name='Comment author'),
        ),
    ]
