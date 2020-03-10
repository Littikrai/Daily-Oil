from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from Post.models import Post

# Create your views here.

def post(request):
    return render(request, 'post.html')


def create_post(request):
    if not request.user.is_superuser:
        return redirect('post')
    msg = ''
    print(request.method)
    if request.method == "POST":
        status = 'S'
        if(request.POST.get('status') == 'on'):
            status = 'H'
        post = Post.objects.create(
            user_id = request.user,
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            create_time = timezone.now(),
            updates_time = timezone.now(),
            status = status
        )
        print('hiddddddd')
        msg = "สร้างสำเร็จแล้ว"
        context = {
            'msg':msg
        }
        return render(request, 'post.html', context=context)
    else:
        post = Post.objects.none()
    context = {
        'post': post
    }
    return render(request, 'createPost.html', context=context)

def updates(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        msg = ''
    except Post.DoesNotExist:
        return redirect('post.html')
    
    if request.method == 'POST':
        status = 'S'
        if(request.POST.get('status') == 'on'):
            status = 'H'
        post.title = request.POST.get('title'),
        post.content = request.POST.get('content'),
        post.updates_time = timezone.now(),
        status = status
        post.save()
        msg = 'อัพเดท Post สำเร็จ'
    context={
        'post':post,
        'msg':msg
    }
    return render(request, 'updatePost.html', context=context)
