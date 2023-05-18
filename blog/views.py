from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from django.http import HttpResponseForbidden
from django.urls import reverse

from .models import Post, Tag, Comment
from .forms import CommentForm


class index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        aggregated_data = {}
        grouped_data = Post.objects.filter(published=True)
        for post in grouped_data:
            year = post.publish_date.strftime('%Y')
            month = post.publish_date.strftime('%b')
            if year not in aggregated_data:
                aggregated_data[year] = {}
            if month not in aggregated_data[year]:
                aggregated_data[year][month] = []
            aggregated_data[year][month].append(post)

        context['archive'] = aggregated_data

        return context


class postDetailView(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'

    def get_context_data(self, *args, **kwargs):
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
