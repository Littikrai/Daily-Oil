from django.db import models
from django.contrib.auth.models import User
from Post.models import Post
# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
