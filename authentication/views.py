from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'authentication/index.html')

def signup(request):

    if request.method == "POST":
        username =request.POST['username']
        first_name =request.POST['first_name']
        last_name =request.POST['last_name']
        email =request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']

        myuser = User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
        myuser.save()

        messages.success(request, "Account Created Successfully")

        return redirect('signin')

    return render(request,'authentication/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            first_name=user.first_name
            return render(request,'authentication/index.html',{'first_name':first_name})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')


    return render(request,'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request,'Logout Successfully!!!')
    return redirect('home')