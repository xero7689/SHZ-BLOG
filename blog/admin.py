from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from PIL import Image as PilImage

from martor.widgets import AdminMartorWidget

from .models import Profile, Tag, Post, Comment, Category, Image

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


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'image_preview',
        'upload_at',
        'image_url'
    ]

    def image_preview(self, obj):
        image = PilImage.open(obj.image.path)

        # Set the maximum width and height for the image
        MAX_WIDTH = 200
        MAX_HEIGHT = 200

        # Calculate the new width and height while maintaining aspect ratio
        width, height = image.size
        if width > MAX_WIDTH:
            scale = MAX_WIDTH / width
            width = int(width * scale)
            height = int(height * scale)
        if height > MAX_HEIGHT:
            scale = MAX_HEIGHT / height
            height = int(height * scale)
            width = int(width * scale)

        # Resize the image
        # image.thumbnail((width, height))
        return format_html(f'<img src={obj.image.url} with="{width}px" height="{height}px"></img>')

    def image_url(self, obj):
        return obj.image.url

    image_url.short_description = "Image URL"
