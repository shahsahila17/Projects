from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def shop1(request):
    return render(request,'shop1.html')
def electronics(request):
    return render(request,'electronics.html')
def utensils(request):
    return render(request,'utensils.html')
def sports1(request):
    return render(request,'sports1.html')
def cloth(request):
    return render(request,'cloth.html')
def amz(request):
    return render(request,'amz.html')
def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            messages.info(request,'Password not matching...')
            return redirect("signup")
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username exists...')
            return redirect("signup")
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists...')
            return redirect("signup")
        user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        user.save()
        return render(request,'login.html')
    return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials...')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')