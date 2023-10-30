from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def homePage(request):
    return render(request,'home.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            return HttpResponse("Incorrect credentials")
    else:
        return render(request,'login.html')


def signupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1!=password2:
            return HttpResponse("Passwords do not match")
        else:
            userNew = User.objects.create_user(username,email,password1)
            userNew.save()
            return redirect('login.html')
    else:
        return render(request,'signup.html')


def logoutPage(request):
    logout(request)
    return redirect('login')