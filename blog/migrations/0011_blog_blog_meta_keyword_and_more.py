# Generated by Django 4.2 on 2023-06-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_profile_blog_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_meta_keyword',
            field=models.CharField(default='blog', max_length=128),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_meta_description',
            field=models.CharField(default='Blog <meta> description', max_length=128),
        ),
    ]
