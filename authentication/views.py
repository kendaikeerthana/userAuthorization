from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

import authentication
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        myuser = User.objects.create_user(username,email,password)
        myuser.firstname = firstname
        myuser.lastname = lastname
        
        myuser.save()
        # the above code is to get the details from the html page and store it in db
        
        messages.success(request,"Your Account has been successfully created")
        return redirect('signin')
    
    return render(request,"authentication/signup.html")
    

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass1']
        
        # to authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"authentication/index.html",{'fname':fname})
        else:
            messages.error(request,"Add credentials")
            return redirect('home')
            
            
    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully! ")
    return redirect('home')