# Generated by Django 4.2 on 2023-06-07 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.TextField(),
        ),
    ]
