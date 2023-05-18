from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import Profile, Tag, Post, Comment, Category

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'website',
        'biography'
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published"
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author',
        'body',
        'comment_at'
    ]

    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget}
    }
