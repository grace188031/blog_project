# Generated by Django 5.0.8 on 2024-08-10 00:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comments_create_date_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 10, 0, 39, 15, 338542, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 10, 0, 39, 15, 338188, tzinfo=datetime.timezone.utc)),
        ),
    ]
