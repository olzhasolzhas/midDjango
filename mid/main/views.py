from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib import messages
from .models import Man


def index(request):
    user = Man.objects.all()
    context = {
        'user': user
    }
    return render(request, 'index.html', context=context)


def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    else:
        form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, 'register.html', context=context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')
        context = {}
        return render(request, 'login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')
