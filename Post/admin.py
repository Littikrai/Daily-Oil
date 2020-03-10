from django.contrib import admin
from django.contrib.auth.models import Permission
from Post.models import Post

# Register your models here.
admin.site.register(Permission)

admin.site.register(Post)