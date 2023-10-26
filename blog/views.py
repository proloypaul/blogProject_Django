from django.shortcuts import render
from .models import PostBlog


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




def home(request):
    postedBlog = PostBlog.objects.all()
    return render(request, 'blog/home.html', {"blogPost": postedBlog})

def about(request):
    return render(request, 'blog/about.html', {"title":"about page"})