from django.db import models
from django.conf import settings
from django.urls import reverse

from martor.models import MartorField


class Blog(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    blog_title = models.CharField(max_length=32, default="Blog Title", unique=True)
    blog_subtitle = models.CharField(max_length=64, default="Blog Subtitle")
    blog_meta_description = models.CharField(
        max_length=128, default="Blog <meta> description"
    )
    blog_meta_keywords = models.CharField(max_length=128, default="blog")

    def __str__(self):
        return self.blog_title


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    nickname = models.CharField(max_length=16, default="Author Nick Name")
    website = models.URLField(blank=True)
    biography = models.TextField()

    twitter_name = models.CharField(max_length=64, blank=True)
    facebook_name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.get_username()


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"name": self.name})


class Image(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BasePostModel(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    abstract = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = MartorField()
    meta_desc = models.CharField(max_length=150, blank=True)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(auto_now=True)

    cover_image = models.ForeignKey(
        Image, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True
    )

    def get_absolute_url(self):
        raise NotImplementedError("Subclasses must implement get_absolute_url()")

    def __str__(self):
        return self.title


class Post(BasePostModel):
    class Meta(BasePostModel.Meta):
        ordering = ['-publish_date']

    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={
                "slug": self.slug,
                "year": self.created_date.year,
                "month": self.created_date.month,
                # "day": self.created_date.day
            },
        )


class SideProject(BasePostModel):
    class Meta(BasePostModel.Meta):
        ordering = ['created_date']

    project_owner = models.ForeignKey(Profile, on_delete=models.PROTECT)
    link = models.URLField()


class Comment(models.Model):
    author = models.CharField(max_length=128, default='Anonymous')
    body = MartorField()
    approved = models.BooleanField(default=True)
    comment_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}:「{self.body[:20]}...」'


class Visitor(models.Model):
    remote_addr = models.CharField(max_length=64, default="", blank=True, null=True)
    user_agent = models.CharField(max_length=512, default="", blank=True, null=True)
    http_referer = models.CharField(max_length=512, default="", blank=True, null=True)
    path_info = models.CharField(max_length=128, default="", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.remote_addr}'
