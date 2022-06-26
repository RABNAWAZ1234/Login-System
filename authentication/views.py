from email import message
import http
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'authentication/index.html')

def signup(request):

    if request.method=='POST':
        username=request.POST['user_name']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password11=request.POST['password11']
        password1=request.POST['password1']
        if User.objects.filter(username=username):
            messages.error(request,'user name is already taken. Please choose another one ')
            return redirect('signu')
        my_user=User.objects.create_user(username,email,password11)
        my_user.first_name=fname
        my_user.last_name=lname
        my_user.save()
        messages.success(request,'Your account has been successfully created')

        # Welcome TO Email
        subject="Welcome! in Email Account"
        message='Please'
        from_email=settings.EMAIL_HOST_USER
        to_list=[my_user.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)



        return redirect('/signin')
    return render(request,'authentication/signup.html')

def signin(request):

    if request.method=='POST':
        username1=request.POST['username']
        password11=request.POST['password11']
        user=authenticate(username=username1,password=password11)
        if user is not None:
            fname=user.first_name
            login(request,user)
            return render(request,"authentication/work.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credential")
            return HttpResponse("User name or password is not correct")
           
    return render(request,'authentication/signin.html')


def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect('home')
   
    
    

def work(request):
    return render(request,'authentication/work.html')