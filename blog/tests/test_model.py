from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from blog.models import Blog, Profile, Tag, Category, Image, Post, Comment, Visitor


class BlogModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )
        self.blog = Blog.objects.create(user=user)

    def test_str(self):
        self.assertEqual(str(self.blog), "Blog Title")


class ProfileModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )
        self.profile = Profile.objects.create(user=user)

    def test_str(self):
        self.assertEqual(str(self.profile), "testuser")


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")

    def test_str(self):
        self.assertEqual(str(self.tag), "Test Tag")


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_str(self):
        self.assertEqual(str(self.category), "Test Category")

    def test_get_absolute_url(self):
        url = reverse("category_detail", kwargs={"name": self.category.name})
        self.assertEqual(self.category.get_absolute_url(), url)


class ImageModelTest(TestCase):
    def setUp(self):
        self.image = Image.objects.create(name="Test Image")

    def test_str(self):
        self.assertEqual(str(self.image), "Test Image")


class PostModelTest(TestCase):
    def setUp(self):
        author = Profile.objects.create(
            user=get_user_model().objects.create_user(
                username="testuser", email="testuser@example.com", password="testpass"
            )
        )
        category = Category.objects.create(name="Test Category")
        image = Image.objects.create(name="Test Image")

        self.post = Post.objects.create(
            title="Test Post",
            abstract="Test Abstract",
            slug="test-post",
            body="Test Body",
            author=author,
            category=category,
            cover_image=image,
            published=True,
        )

    def test_str(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_get_absolute_url(self):
        url = reverse(
            "post_detail", kwargs={"slug": self.post.slug, "year": self.post.created_date.year, "month": self.post.created_date.month}
        )
        self.assertEqual(self.post.get_absolute_url(), url)


class CommentModelTest(TestCase):
    def setUp(self):
        post = Post.objects.create(
            title="Test Post",
            abstract="Test Abstract",
            slug="test-post",
            body="Test Body",
            author=Profile.objects.create(
                user=get_user_model().objects.create_user(
                    username="testuser", email="testuser@example.com", password="testpass"
                )
            ),
            published=True,
        )

        self.comment = Comment.objects.create(
            author="Test Author", body="Test Body", post=post, approved=True
        )

    def test_str(self):
        self.assertEqual(str(self.comment), "Test Author:「Test Body...」")


class VisitorModelTest(TestCase):
    def setUp(self):
        self.visitor = Visitor.objects.create(
            remote_addr="127.0.0.1",
            user_agent="Test User Agent",
            http_referer="http://example.com",
            timestamp="2000-01-01T00:00:00Z",
        )

    def test_str(self):
        self.assertEqual(str(self.visitor), "127.0.0.1")