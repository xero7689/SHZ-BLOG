# Generated by Django 4.2 on 2023-06-09 03:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0008_alter_profile_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blog_subtitle',
            field=models.CharField(default='Blog Subtitle', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='blog_title',
            field=models.CharField(default='Blog Title', max_length=32),
            preserve_default=False,
        ),
    ]
