# Generated by Django 4.2 on 2023-05-05 15:38

from django.db import migrations
import martor.models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=martor.models.MartorField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=martor.models.MartorField(),
        ),
    ]
