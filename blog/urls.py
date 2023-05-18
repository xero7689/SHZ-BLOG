from django.urls import path

from . import views

urlpatterns = [
    path('posts/<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.postView.as_view(), name='post_detail'),
    path('tags/', views.TagsListView.as_view(), name='tags_list'),
    path('tags/<str:name>/', views.tag_detail_view, name='tag_detail'),
    path('<int:year>/<int:month>/', views.index.as_view(), name='index'),
    path('<int:year>/', views.index.as_view(), name='index'),
    path('', views.index.as_view(), name='index'),
]
