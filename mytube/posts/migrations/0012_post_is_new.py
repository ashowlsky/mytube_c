# Generated by Django 2.2 on 2020-02-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_post_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
    ]
