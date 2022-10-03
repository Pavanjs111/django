# Create your views here.
from django.shortcuts import render

# Create your views here.
from asdapp.forms import Userform
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def registration(request):
    registered =False
    if request.method=='POST':
        user_form=Userform(request.POST)
        # profile_form=UserProfileInfoForms(request.POST)

        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registered=True
        else:
            print(user_form.errors)
    else:
        user_form=Userform()
        # profile_form=UserProfileInfoForms()
    return render(request,'registration.html',{'user_form':user_form,'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("user is not active")
        else:
            return HttpResponse("invalid credential")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



