# Generated by Django 3.1 on 2020-08-17 10:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0026_auto_20200816_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='comment',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
