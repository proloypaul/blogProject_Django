from django.contrib import admin
from .models import PostBlog

# Register your models here.
@admin.register(PostBlog)
class PostBlogAdmin(admin.ModelAdmin):
    list_display = ["id", "creatorName", "blogImage", "title", "description", "category", "publishDate", "author"]