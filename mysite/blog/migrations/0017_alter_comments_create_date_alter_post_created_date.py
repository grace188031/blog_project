# Generated by Django 5.0.8 on 2024-08-10 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_comments_create_date_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 10, 0, 47, 44, 72808, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 10, 0, 47, 44, 72419, tzinfo=datetime.timezone.utc)),
        ),
    ]
