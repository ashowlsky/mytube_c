# Generated by Django 2.2 on 2020-02-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20200223_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
