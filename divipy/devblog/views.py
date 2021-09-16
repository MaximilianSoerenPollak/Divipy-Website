from django.http import request
from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "devblog/home.html", context)


def about(request):
    return render(request, "devblog/about.html")

class PostListView(ListView):
    model = Post
    template_name = "devblog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post


class PostCreateView(UserPassesTestMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # Test if user is ADMIN OR NOT
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.error(self.request, "You have no permission to view this page.")
        return redirect("devblog-home")

class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # Test if user is ADMIN OR NOT
        post = self.get_object()
        if self.request.user == post.author and self.request.user.is_superuser:
            return True
        else:
            return False

    
    def handle_no_permission(self):
        messages.error(self.request, "You have no permission to view this page.")
        return redirect("devblog-home")


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/devblog"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # Test if user is ADMIN OR NOT
        post = self.get_object()
        if self.request.user == post.author and self.request.user.is_superuser:
            return True
        else:
            return False
    
    def handle_no_permission(self):
        messages.error(self.request, "You have no permission to view this page.")
        return redirect("devblog-home")