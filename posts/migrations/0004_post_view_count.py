# Generated by Django 3.1 on 2020-09-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
