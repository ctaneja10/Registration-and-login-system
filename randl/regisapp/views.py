from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'files/home.html')

def creationpage(request):
    return render(request, 'files/creation.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpass = request.POST.get('cpass')
        if password != cpass:
            messages.warning(request, "Password does not match")
            return redirect('home')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw=request.POST.get('pass')
        user = authenticate(username=uname, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.warning(request, 'Invalid credentials, please try again')
            return redirect('home')
    return HttpResponse('404 - Not found')

def handleLogout(request):
    logout(request)
    return redirect('home')






