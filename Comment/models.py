from django.db import models
from Post.models import Post
# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
