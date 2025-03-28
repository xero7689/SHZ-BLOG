# Generated by Django 4.2 on 2023-06-09 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_profile_blog_subtitle_profile_blog_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='blog_subtitle',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='blog_title',
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'blog_title',
                    models.CharField(default='Blog Title', max_length=32, unique=True),
                ),
                (
                    'blog_subtitle',
                    models.CharField(default='Blog Subtitle', max_length=64),
                ),
                (
                    'blog_meta_description',
                    models.CharField(default='Blog <meta> description', max_length=150),
                ),
                (
                    'user',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
