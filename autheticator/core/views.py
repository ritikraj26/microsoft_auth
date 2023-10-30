from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

def homePage(request):
    return render(request,'home.html')


def loginPage(request):
    return render(request,'login.html')


def signupPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        userNew = User.objects.create_user(username,email,password1)
        userNew.save()
        return HttpResponse("User creted")
    else:
        return render(request,'signup.html')
