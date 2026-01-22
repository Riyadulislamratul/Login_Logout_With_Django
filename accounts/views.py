from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        User.objects.create_user(
            username = request.POST.get("username"),
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            email = request.POST.get("email"),
            phone = request.POST.get("phone"),
            password = request.POST.get("password")

            )
        return redirect('user_login')
        

    return render(request, 'register.html')
    


