from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post, Tag


def index(request):
    posts = Post.objects.all()[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


class postDetailView(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'


class TagsListView(ListView):
    model = Tag
    template_name = 'blog/tagsList.html'


def tag_detail_view(request, name):
    tag = Tag.objects.get(name=name)
    posts = tag.post_set.all()

    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'blog/tagDetail.html', context)
