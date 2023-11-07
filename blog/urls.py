from django.urls import path
from . import views
from .views import PostListView, PostDetailsView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="homePage"),
    path('post/<int:pk>', PostDetailsView.as_view(), name="postDetails"),
    path('post/new', PostCreateView.as_view(), name="createPost"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="postUpdate"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="postDelete"),
    # path('', views.home, name="homePage"),
    path('about/', views.about, name="aboutPage"),
]
