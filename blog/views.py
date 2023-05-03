from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from django.http import HttpResponseForbidden
from django.urls import reverse

from .models import Post, Tag, Comment
from .forms import CommentForm


def index(request):
    posts = Post.objects.all()[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


class postDetailView(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comment.objects.filter(post=self.get_object())

        context['form'] = CommentForm()
        context['comments'] = comments

        return context


class LeaveCommentFormView(SingleObjectMixin, FormView):
    template_name = 'blog/postDetail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()

        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save(self.object)

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_detail', kwargs={"slug": self.object.slug})


class postView(View):
    def get(self, request, *args, **kwargs):
        view = postDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = LeaveCommentFormView.as_view()
        return view(request, *args, **kwargs)


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
