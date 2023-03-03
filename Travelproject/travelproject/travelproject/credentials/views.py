from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
def signup(request):
    if request.method=='POST':
        firstname = request.POST['name1']
        lastname = request.POST['name2']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pswsd']
        CPASSWORD = request.POST['cpswsd']
        if CPASSWORD==password:
            if  User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=firstname,
                                         last_name=lastname,
                                         email=email,
                                         username=username,
                                         password=password)
                user.save();
            return redirect('login')
        else:
            messages.info(request, "password not matching!!!")
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswsd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')