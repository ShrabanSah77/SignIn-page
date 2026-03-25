from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "credentials")

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'All fields are required')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'dashboard.html')

def forgot_password(request):
    if request.method =='POST':
        email = request.POST['email']
        messages.success(request, 'Password reset link sent (check console)')
    return render(request, 'forgot_password.html')

