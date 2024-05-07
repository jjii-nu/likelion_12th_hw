from django.db import models
from django.contrib.auth.models import User  # User 모델 import

from main.models import Post

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
