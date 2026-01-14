from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request,"base.html")

def HomePage(request):
    return render(request,"HomePage.html")

def BlogRegister(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        case1 = User.objects.filter(username = username).exists()
        case2 = User.objects.filter(email=email).exists()
        
        if case1:
            messages.error(request,"Username Already Exists ...")
            return redirect('base')
        if case2 : 
            messages.error(request,"Email Already Exists .. please login")
            return redirect("base")
        
        User.objects.create_user(
            first_name=first_name,
            last_name = last_name,
            email=email,
            username=username,
            password=password
        )
        messages.success(request,"Account Created please logged In")
        return redirect('BlogLogin')
    
    return render(request,"BlogRegister.html")

def BlogLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username , password = password)
        
        if not user:
            messages.error(request,"Username doesnot exists ...")
            return redirect('BlogRegister')
        
        login(request,user)
        messages.success(request,"Logged In Successful")
        return redirect("HomePage")
    
    return render(request,"BlogLogin.html")

def BlogLogout(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please Logged In first")
        return redirect("base")
    logout(request)
    return redirect('base')