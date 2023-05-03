from django.urls import path

from . import views

urlpatterns = [
    path('posts/<slug:slug>/', views.postView.as_view(), name='post_detail'),
    path('tags/', views.TagsListView.as_view(), name='tags_list'),
    path('tags/<str:name>/', views.tag_detail_view, name='tag_detail'),
    path('', views.index, name='index'),
]
