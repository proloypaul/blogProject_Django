from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import PostBlog
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# blogPost = [
#     {
#         "title": "what is OOP",
#         "description": "some description about our blog",
#         "author": "Suprit",
#         "pubilsh": "12/2/23"
#     },
#     {
#         "title": "How react dom work",
#         "description": "some description about our blog",
#         "author": "Suprit",
#         "pubilsh": "12/2/23"
#     }
# ]




# def home(request):
#     postedBlog = PostBlog.objects.all()
#     return render(request, 'blog/home.html', {"blogPost": postedBlog})

class PostListView(ListView):
    model = PostBlog
    template_name = 'blog/home.html'
    context_object_name = 'blogPost'
    ordering = ['-publishDate']

class PostDetailsView(DetailView):
    model = PostBlog
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = PostBlog
    fields = ['blogImage', 'title', 'description']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = PostBlog
    fields = ['title', 'description']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

class PostDeleteView(DeleteView):
    model = PostBlog
    template_name = 'blog/delete_post.html'
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False

def about(request):
    return render(request, 'blog/about.html', {"title":"about page"})


