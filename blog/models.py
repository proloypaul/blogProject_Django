from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PostBlog(models.Model):
    creatorName = models.CharField(max_length=50)
    # blogImg = models.ImageField()
    title = models.TextField()
    description = models.TextField()
    category = models.CharField(max_length=50)
    publishDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

