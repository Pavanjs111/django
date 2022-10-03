# from operator import imod
from django.urls import reverse
from xml.dom.domreg import registered
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from userapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

def register(request):

    registered=False

    if request.method =='POST':
        user_form=UserForm(request.POST)
        profile_form=UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():#this is for validating the form
            user=user_form.save() # we are using another variablt to use the form 
            user.set_password(user.password)#we are taking the password form registerd html
            user.save()# we are saving the variable that contains user_form

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profilepics' in request.FILES:
                profile.profilepics=request.FILES['profilepics']
            
            profile.save()

            registered=True
        
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,"register.html",{'user_form':user_form,
                                           'profile_form':profile_form,
                                            'registered':registered})


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
                return HttpResponse('user is not acctive')
        else:
            return HttpResponse('invalid cred')
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



