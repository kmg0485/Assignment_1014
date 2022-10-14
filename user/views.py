from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as loginsession


# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        
        if password == password:
            User.objects.create_user(username = username, password = password, phone = phone, address = address)
            return redirect("/login")
        else:
            return HTTPResponse("비번 오류")
        
    else:    
        return HttpResponse("허용되지 않는 메소드입니다.")
    
    
def login(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/home')
        else:
            return render(request,'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginsession(request, user)
            return redirect('user:user')
        else: 
            return render(request,'login.html',{'error':'이메일 혹은 패스워드를 확인 해 주세요'}) 
        
def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    else:
        return redirect('/login')


