# Generated by Django 2.2 on 2020-02-22 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='new',
        ),
    ]
