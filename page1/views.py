from django.shortcuts import redirect, render ,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'base.html')

def rent(request):
    return render(request,'listing.html')

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_again = request.POST['password_again']

           
        if password != password_again:
            messages.error(request,'Password not matched.')
            return redirect('/register')
        else:
            user = User.objects.create_user(username,email,password)
            user.save()
            messages.success(request,'Account has been created Successfully')
            return redirect('/login')

    

    return render(request,'register.html')


def login_process(request):
    
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(request, username=loginusername , password=loginpassword)


        if user is not None:
            login(request,user)
            return redirect('/rent')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('/login')
    
    return render(request,'login.html')



