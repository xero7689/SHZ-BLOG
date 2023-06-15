from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

from blog.models import Blog, Profile, Tag, Category, Image, Post, Comment, Visitor
from blog.views import index
from blog.forms import CommentForm


class TestIndexView(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass"
        )
        Blog.objects.create(user=user, blog_title="Test Blog")

        category = Category.objects.create(name="Test Category")
        profile=Profile.objects.create(user=user)

        tag1 = Tag.objects.create(name="Test Tag 1")
        tag2 = Tag.objects.create(name="Test Tag 2")

        post1 = Post.objects.create(
            title="Test Post 1",
            abstract="Test Abstract 1",
            slug="test-post-1",
            body="Test Body 1",
            author=profile,
            category=category,
            published=True,
            publish_date=timezone.now(),
            created_date=timezone.now(),
        )
        post1.tags.add(tag1, tag2)

        post2 = Post.objects.create(
            title="Test Post 2",
            abstract="Test Abstract 2",
            slug="test-post-2",
            body="Test Body 2",
            author=profile,
            category=category,
            published=False,
            publish_date=timezone.now(),
            created_date=timezone.now(),
        )
        post2.tags.add(tag2)

    def test_get_queryset_returns_published_posts_only(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(len(response.context['posts']), 1)

    def test_get_queryset_returns_posts_sorted_by_publish_date(self):
        post1 = Post.objects.get(slug="test-post-1")
        post2 = Post.objects.get(slug="test-post-2")

        post2.created_date = post1.publish_date - timezone.timedelta(days=1)
        post2.save()

        response = self.client.get(reverse('posts'))
        self.assertEqual(list(response.context['posts']), [post1])

    def test_get_queryset_returns_posts_filtered_by_year_and_month(self):
        post1 = Post.objects.get(slug="test-post-1")
        post1.created_date = timezone.datetime(2000, 1, 1, tzinfo=timezone.utc)
        post1.save()

        post2 = Post.objects.get(slug="test-post-2")
        post2.created_date = timezone.datetime(2001, 1, 1, tzinfo=timezone.utc)
        post2.save()

        response1 = self.client.get(reverse('posts', kwargs={"year": "2000"}))
        self.assertEqual(list(response1.context['posts']), [post1])

        response2 = self.client.get(reverse('posts', kwargs={"year": "2000", "month": "1"}))
        self.assertEqual(list(response2.context['posts']), [post1])

    def test_search_query_filters_queryset_by_title(self):
        response = self.client.get(reverse('posts') + "?q=test")
        self.assertEqual(len(response.context['posts']), 1)

    def test_search_query_returns_not_found_message_when_no_results(self):
        response = self.client.get(reverse('posts') + "?q=fail")
        self.assertEqual(response.context['not_found_message'], "No results found for your search query fail")

    def test_search_query_returns_empty_not_found_message_when_results_found(self):
        response = self.client.get(reverse('posts') + "?q=Test")
        self.assertEqual(response.context['not_found_message'], "")

