from django.db import models

# Create your models here.
class Blogcreator(models.Model):
    creatorName = models.CharField(max_length=50)
    # blogImg = models.ImageField()
    blogTitle = models.TimeField()
    description = models.TextField()
    blogCategory = models.CharField(max_length=50)
    publishDate = models.DateTimeField()


