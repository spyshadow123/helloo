from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import My,MediaFile,Style_JS

# Create your views here.
def home(r):
    return render(r,'home.html')
def about(r):
    return render(r,'about.html')
def pre(r):
    return render(r,'pre.html')
def secure(r):
    obj=MediaFile.objects.filter(id=1)
    return render(r,'secure.html',{'video':obj})
def register(r):
    if r.method=='POST':
        username=r.POST['name']
        pwd=r.POST['pwd']
        if User.objects.filter(username=username).exists():
            messages.info(r,'User already exist')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=pwd)
            user.save()
            messages.info(r,'User created Successfully')
            return redirect('login')
    else:
        return render(r,'register.html')
def login(r):
    if r.method=='POST':
        username=r.POST['name']
        pwd=r.POST['pwd']
        log=auth.authenticate(username=username,password=pwd)
        if log is not None:
            auth.login(r,log)
            messages.info(r,'successfully login')
            return redirect('secure')
        else:
            messages.info(r,'wrong information')
            return redirect('login')
    else:
        return render(r,'login.html')
def logout(r):
    auth.logout(r)
    messages.info(r,'logout successfully')
    return render(r, 'home.html')
def contact(r):
    if r.method=='POST':
        if r.POST['name']and r.POST['email']and r.POST['mobile']and r.POST['message'] :
            record=My()
            record.name=r.POST['name']
            record.email=r.POST['email']
            record.mobile=r.POST['mobile']
            record.message=r.POST['message']
            record.save()
            messages.info(r,'Your Input is Received ,Thanks !')
            return render(r,'contact.html')
    else:
        obj=Style_JS.objects.filter(id=1)
        return render (r,'contact.html',{"key":obj})
def data(r):
    if r.method=='POST':
        user=r.POST['name']
        pwd=r.POST['pwd']
        if user=='aman' and pwd=='aman':
            obj=My.objects.all()
            return render(r,'data.html',{'key':obj})
        else:
            messages.info(r,'wrong credentials')
            return redirect('data')
    return render(r,'data.html')

