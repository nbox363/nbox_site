# Generated by Django 3.1 on 2020-08-12 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200812_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='comment_text',
        ),
    ]
