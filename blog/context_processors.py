from .models import Blog, Profile, Post, Category


def index(request):
    # Blog
    blog = Blog.objects.first()

    # About Me
    profile = Profile.objects.first()

    # Aggregate Archieve Data
    aggregated_data = {}
    grouped_data = Post.objects.filter(published=True).order_by('-created_date')
    for post in grouped_data:
        year = post.created_date.strftime('%Y')
        month = post.created_date.strftime('%m')
        if year not in aggregated_data:
            aggregated_data[year] = {}
        if month not in aggregated_data[year]:
            aggregated_data[year][month] = []
        aggregated_data[year][month].append(post)

    # Categories
    categories = Category.objects.all()

    # Breadcrumb
    paths = list(filter(None, request.path.split('/')))
    breadcrumb_path = []
    for index, path in enumerate(paths):
        breadcrumb_path.append({
            "name": path,
            "href": "/" + "/".join([p for p in paths[:index + 1]])
        })

    return {
        'blog': blog,
        'profile': profile,
        'archive': aggregated_data,
        'categories': categories,
        'breadcrumb_path': breadcrumb_path
    }
