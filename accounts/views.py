from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username = request.POST.get("username"),
            # first_name = request.POST.get("first_name"),
            # last_name = request.POST.get("last_name"),
            email = request.POST.get("email"),
            # phone = request.POST.get("phone"),
            password = request.POST.get("password")
            )
        return redirect('user_login')
        

    return render(request, 'register.html')
    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credentials. Please try again.")
    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')
