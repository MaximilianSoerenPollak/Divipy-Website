from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="devblog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="devblog-postdetail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="devblog-postupdate"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="devblog-postdelete"),
    path("post/new/", PostCreateView.as_view(), name="devblog-create"),
    path("about", views.about, name="devblog-about")
]
