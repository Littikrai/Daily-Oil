from django.shortcuts import render, redirect
from django.utils import timezone
from Comment.models import Comment
from Post.models import Post

# Create your views here.
def add_comment(request, post_id):
    if request.method == 'POST':
        comment = Comment.objects.create(
            user_id = request.user,
            post_id = Post.objects.get(pk=post_id),
            content = request.POST.get('content'),
            create_time = timezone.now()
        )
        context = {
            'comment':comment
        }
        return redirect(to='detail', post_id=post_id)
    else:
        post = Post.objects.none()

def Delete_comment(request, comment_id, post_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect(to='detail', post_id=post_id)


