from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def handlelogin(request):
        if request.method=="POST":

                username=request.POST['email']
                userpassword=request.POST['pass1']
                myuser=authenticate(username=username,password=userpassword)

                if myuser is not None:
                        login(request,myuser)
                        # messages.success(request,"Login Success")
                        return redirect('/')

                else:
                        messages.error(request,"Invalid Credentials")
                        return redirect('/')
        
        return render(request,'login.html')
def handlelogout(request):
        logout(request)
        messages.info(request,"Logout Success")
        return redirect('/')




