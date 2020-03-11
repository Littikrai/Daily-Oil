from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from Post.models import Post
from Comment.models import Comment

# Create your views here.

def post(request):
    post = Post.objects.all()
    comment = Comment.objects.all()
    search_txt = request.GET.get('inputSearch', '')
    print(search_txt)
    if search_txt:
        post = Post.objects.filter(
            title__icontains=search_txt
        )
    msg = ''
    context = {
        'post':post,
        'comment':comment
    }
    return render(request, 'post.html', context=context)


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
    print(post.content)  
    status = 'S'
    if request.method == 'POST':
        if(request.POST.get('status') == 'on'):
            status = 'H'
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.updates_time = timezone.now()
        post.status = status
        post.save()
        msg = 'อัพเดท Post สำเร็จ'
        return redirect(to='detail', post_id=post_id)
    context={
        'post':post,
        'msg':msg
    }
    return render(request, 'updates.html', context=context)

def hide_post(request, post_id, status):
    try:
        post = Post.objects.get(pk=post_id)
        msg = ''
    except Post.DoesNotExist:
        return redirect('post.html')
    if request.method == 'GET':        
        post.status = status
        post.save()
    context={
        'post':post,
        'msg':msg
    }
    return redirect('post')


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = Comment.objects.filter(post_id = post_id)
    context={
        'post':post,
        'comment':comment
    }
    return render(request, 'detail.html', context=context)

    
