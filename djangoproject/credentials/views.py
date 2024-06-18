from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Login view
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")

# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password1')
        if not all([username, first_name, last_name, email, password, confirm_password]):
            messages.error(request, "Please fill out all fields")
            return redirect('register')
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('register')

        # If all checks pass, create the user
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, "User created successfully")
        return redirect('login')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
