from django.contrib import auth, messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import data, MyForm


# Create your views here.
def first(request):
    obj = data.objects.all()
    return render(request, "index.html", {'result': obj})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, "invalid data")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')

            elif User.objects.filter(password=password).exists():
                messages.info(request, "weak password")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
            print("new user created")

            user.save();
            return redirect('login')


        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('new')
    return render(request, "register.html")


# def new(request):
#     return render(request, "new.html")


def new(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return redirect('confirm')  # Redirect to a success page
    else:
        form = MyForm()

    return render(request, 'new.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')


def confirm(request):
    return render(request, "confirm.html")
