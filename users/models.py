from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="https://d2v9ipibika81v.cloudfront.net/uploads/sites/210/Profile-Icon.png", upload_to="proifile_pics")