# Generated by Django 4.2 on 2023-06-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0012_rename_blog_meta_keyword_blog_blog_meta_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='Author Nick Name', max_length=16),
        ),
    ]
