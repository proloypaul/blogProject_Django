from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class PostBlog(models.Model):
    creatorName = models.CharField(max_length=50)
    # blogImage = models.ImageField(default="https://d2v9ipibika81v.cloudfront.net/uploads/sites/210/Profile-Icon.png", upload_to="blog_pics")
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    publishDate = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('postDetails', kwargs={'pk': self.pk})