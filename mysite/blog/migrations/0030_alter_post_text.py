# Generated by Django 5.0.8 on 2024-08-13 18:25

import django_quill.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_quill.fields.QuillField(verbose_name=''),
        ),
    ]
