from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', views.home, name='yelp-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', views.post_save, name='post-create'),
    path('about/', views.about, name='yelp-about'),
]