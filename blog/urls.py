from django.urls import path

from . import views
from .views import (PostCreateView, PostDeleteView, PostDetailView,
                    PostListView, PostUpdateView, UserPostListView)

urlpatterns = [
    path(
        '',
        PostListView.as_view(),
        name='blog-home'),
    path(
        'post/new/',
        PostCreateView.as_view(),
        name='post-create'),
    path(
        'post/<int:pk>/delete',
        PostDeleteView.as_view(),
        name='post-delete'),
    path(
        'post/<int:pk>/',
        PostDetailView.as_view(),
        name='post-detail'),
    path(
        'post/<int:pk>/update',
        PostUpdateView.as_view(),
        name='post-update'),
    path(
        'about/',
        views.about,
        name='blog-about'),
    path(
        'user/<str:username>',
        UserPostListView.as_view(),
        name='user-posts'),
]
