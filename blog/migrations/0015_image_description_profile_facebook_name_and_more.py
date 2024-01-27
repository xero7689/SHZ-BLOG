# Generated by Django 4.2 on 2023-06-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0014_post_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_name',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
