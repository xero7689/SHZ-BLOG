from .models import Profile, Post, Category


def index(request):
    # About Me
    profile = Profile.objects.first()

    # Aggregate Archieve Data
    aggregated_data = {}
    grouped_data = Post.objects.filter(published=True)
    for post in grouped_data:
        year = post.publish_date.strftime('%Y')
        month = post.publish_date.strftime('%m')
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
        'profile': profile,
        'archive': aggregated_data,
        'categories': categories,
        'breadcrumb_path': breadcrumb_path
    }
