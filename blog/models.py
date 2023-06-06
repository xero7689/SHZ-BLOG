from django.db import models
from django.conf import settings
from django.urls import reverse

from martor.models import MartorField


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    website = models.URLField(blank=True)
    biography = models.CharField(max_length=240, blank=True)

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


class Post(models.Model):
    class Meta:
        ordering = ['-publish_date']

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    abstract = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = MartorField()
    meta_desc = models.CharField(max_length=150, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            "slug": self.slug,
            "year": self.created_date.year,
            "month": self.created_date.month,
            # "day": self.created_date.day
        })

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=128, default='Anonymous')
    body = MartorField()
    approved = models.BooleanField(default=True)
    comment_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}:「{self.body[:20]}...」'


class Image(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images")
    upload_at = models.DateTimeField(auto_now_add=True)
