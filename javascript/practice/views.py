from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        # if request.POST['password1'] == request.POST['password2']:
        user = User.objects.create_user(
            username=request.POST['id'], password=request.POST['password1'], email=request.POST['email'])
        user.profile.phoneNumber = request.POST['phonenumber']
        user.profile.gender = request.POST['gender']
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(
            request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')
