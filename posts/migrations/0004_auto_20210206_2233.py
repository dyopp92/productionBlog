# Generated by Django 3.1.5 on 2021-02-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_main_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='main_post',
        ),
        migrations.AddField(
            model_name='post',
            name='yt_url',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
