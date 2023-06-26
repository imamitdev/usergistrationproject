from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render (request,'home.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user_name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=user_name,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "login successfully ")
            return redirect('/')
        else:
            messages.error(request, "Invalid User Password ")
            return redirect('/login')

    return render(request,'login.html')
def signup_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method =='POST':
        
        full_name=request.POST['name']
        number=request.POST['number']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=User.objects.filter(username=number).exists()
       
        if len(number)!=10:
            messages.error(request, "Number Should be 10 digit ")
            return redirect('/signup')
        elif password != cpassword:
            messages.error(request, "Password and confirm password did't Match ")
            return redirect('/signup')
        elif user==True:
           messages.error(request, "User Name already Exist")
           return redirect('/signup')
        else:
            user=User.objects.create(username=number,email=email)
            user.password=cpassword
            user.first_name=full_name
            user.save()
            messages.success(request,'Member Successfully Register')
            return redirect('/login')
    return render(request,'Signup.html')

def logout_(request):
    logout(request)
    return redirect('/')