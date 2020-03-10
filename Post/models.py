from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.DateTimeField()
    updates_time = models.DateTimeField()
    status = models.CharField(max_length=2, choices=(('S', 'Show'), ('H', 'hiding')))