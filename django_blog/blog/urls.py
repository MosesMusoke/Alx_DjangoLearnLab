from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView, PostDetailView, CommentUpdateView, CommentDeleteView, CommentCreateView, PostSearchView, PostByTagListView

urlpatterns = [
    path('posts', ListView.as_view(), name='post-list'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/<int:pk>/', DetailView.as_view(), name='post-detail'),
    path('post/new/', CreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', PostSearchView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]
