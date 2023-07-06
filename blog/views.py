from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.urls import reverse

from .models import Post, Tag, Comment, Category, Profile, SideProject
from .forms import CommentForm


class index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    paginate_by = 7

    def get(self, request, *args, **kwargs):
        search_query = self.request.GET.get('q', None)
        if search_query:
            self.object_list = self.get_queryset().filter(title__icontains=search_query)
            if not self.object_list:
                not_found_message = f'No results found for your search query {search_query}'
            else:
                not_found_message = ''
            return self.render_to_response(self.get_context_data(search_query=search_query, not_found_message=not_found_message))
        else:
            self.object_list = self.get_queryset()
            return self.render_to_response(self.get_context_data())

    def get_queryset(self, *args, **kwargs):
        year = self.kwargs.get('year', None)
        month = self.kwargs.get('month', None)

        query_set = super().get_queryset()

        if year:
            query_set = query_set.filter(created_date__year=year)
            if month:
                query_set = query_set.filter(created_date__month=month)

        return query_set.filter(published=True).order_by("-created_date")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = kwargs.get('search_query', None)
        context['not_found_message'] = kwargs.get('not_found_message', '')

        # Date Parameter
        date_parameter = {}
        if 'year' in self.kwargs:
            date_parameter['year'] = self.kwargs['year']
            if 'month' in self.kwargs:
                date_parameter['month'] = self.kwargs['month']

        context['date_parameter'] = date_parameter

        return context


class postDetailView(DetailView):
    model = Post
    template_name = 'blog/postDetail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = Comment.objects.filter(post=self.get_object())

        current_post = self.object
        previous_post = Post.objects.filter(
            created_date__lt=current_post.created_date, published=True).order_by('created_date').last()
        next_post = Post.objects.filter(
            created_date__gt=current_post.created_date, published=True).order_by('created_date').first()

        context['form'] = CommentForm()
        context['comments'] = comments

        context['prev_post'] = previous_post
        context['next_post'] = next_post

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


class CategoryListView(ListView):
    model = Category
    template_name = 'blog/categoryList.html'


def category_detail_view(request, name):
    category = Category.objects.get(name=name)
    posts = category.post_set.all()

    context = {
        'category': category,
        'posts': posts
    }

    return render(request, 'blog/categoryDetail.html', context)


class TagsListView(ListView):
    model = Tag
    template_name = 'blog/tagsList.html'


class SideProjectListView(ListView):
    model = SideProject
    template_name = 'blog/sideProjectList.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)

        return context


def tag_detail_view(request, name):
    tag = Tag.objects.get(name=name)
    posts = tag.post_set.all()

    context = {
        'tag': tag,
        'posts': posts
    }

    return render(request, 'blog/tagDetail.html', context)


def about_view(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }
    return render(request, 'blog/aboutMe.html', context)


def response_error_404_handler(request, exception=None):
    return render(request, 'blog/error404Handler.html', status=404)


def robots_txt(request):
    if request.method == "GET":
        lines = [
            "User-Agent: *",
            "Allow: /",
        ]
        return HttpResponse("\n".join(lines), content_type='text/plain')
    else:
        return HttpResponseNotAllowed(["POST"])
