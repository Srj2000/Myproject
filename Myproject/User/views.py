from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Mypost
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect


def register(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        psk1=request.POST.get('password1')
        psk2=request.POST.get('password2')
        if psk1==psk2:
            myuser=User.objects.create_user(username,email, psk1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            return render(request, 'user/register.html', {'msg':'Your account has created'})
        else:
            return redirect('/')
    return render(request, 'user/register.html')



def post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            post=request.POST.get('post')
            mypost=Mypost(user=request.user, text=post)
            mypost.save()
            return redirect('/post')
    post=Mypost.objects.all()
    return render(request, 'post/post.html', {'msg':post})

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        psk=request.POST.get('password')
        user=authenticate(username=username,password=psk)
        if user is not None:
            login(request,user)
            return redirect('/post')
        else:
            return render(request, 'user/register.html', {"msg":"Wrong Credentials"})
    return render(request, 'user/register.html')

def logoutuser(request):
    logout(request)
    return redirect('/post')

def delt(request,pk):
    post=Mypost.objects.get(id=pk)
    post.delete()
    
    return redirect('/post')

def upd(request,pk):
    if request.method=='POST':
        text=request.POST.get('update')
        print(text)
        post=Mypost.objects.get(id=pk)
        post.text=text
        post.save()
        
        return redirect('/post')
# Create your views here.
