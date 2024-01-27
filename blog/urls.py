from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path(
        'side-projects/', views.SideProjectListView.as_view(), name='side_project_list'
    ),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<str:name>', views.category_detail_view, name='category_detail'),
    path(
        'posts/<int:year>/<int:month>/<slug:slug>/',
        views.postView.as_view(),
        name='post_detail',
    ),
    path('posts/', views.index.as_view(), name="posts"),
    path('posts/<int:year>/<int:month>/', views.index.as_view(), name='posts'),
    path('posts/<int:year>/', views.index.as_view(), name='posts'),
    path('tags/', views.TagsListView.as_view(), name='tags_list'),
    path('tags/<str:name>/', views.tag_detail_view, name='tag_detail'),
    path('', views.index.as_view(), name='index'),
]
