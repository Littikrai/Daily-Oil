from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('post')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'
    return render(request, template_name='login.html', context=context)

def add_user(request):
    if request.user.id:   
        return redirect('login')       
    else:
        msg = ''
        context = {}
        if request.method == 'POST':
            context['username'] = request.POST.get('username')
            context['email'] = request.POST.get('email')
            context['first_name'] = request.POST.get('first_name')
            context['last_name'] = request.POST.get('last_name')
            if(request.POST.get('password') != request.POST.get('confirm_password')):
                err = 'password ไม่ตรงกัน'
                context['err'] = err
                print(0)
                return render(request, 'register.html', context=context)
            else:
                try:
                    user = User.objects.create_user(
                        request.POST.get('username'),
                        request.POST.get('email'),
                        request.POST.get('password'),
                    )
                    user.first_name = request.POST.get('first_name')
                    user.last_name = request.POST.get('last_name')
                    user.save()
                    msg = 'สร้างสำเร็จแล้วไปเขียนบทความเจ๋ง ๆ ได้เลยจร้า เย่!!'
                except IntegrityError:
                    err = 'username มีคนใช้แล้ว'
                    context['err'] = err
                    return render(request, 'register.html', context=context)
        else:
            user = User.objects.none()
        context = {
            'name':user,
            'msg':msg
        }
        return render(request, 'register.html', context=context)        
   

def user_logout(request):
    logout(request)
    return redirect('post')