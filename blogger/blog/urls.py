from django.urls import path
from .views import (
    HomeView, 
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
]