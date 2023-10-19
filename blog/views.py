from django.shortcuts import render
from django.http import HttpResponse

blogPost = [
    {
        "title": "what is OOP",
        "description": "some description about our blog",
        "author": "Suprit",
        "pubilsh": "12/2/23"
    },
    {
        "title": "How react dom work",
        "description": "some description about our blog",
        "author": "Suprit",
        "pubilsh": "12/2/23"
    }
]

def home(request):
    return render(request, 'blog/home.html', {"blogPost": blogPost})

def about(request):
    return render(request, 'blog/about.html', {"title":"about page"})