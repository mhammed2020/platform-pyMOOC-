from django.shortcuts import render, redirect
from . forms import UserRegister, LoginForm
from . forms import ProfileForm, ProfileFormUser
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . models import Profile

# reacptcha

import requests 
from django.conf import settings

from django.contrib.auth.models import  auth,User
def home(request) :


    return render ( request, 'blog/home.html')

def register_view(request) :
    if request.method =='POST':
        obj = UserRegister(request.POST)
        
        print("******",obj.__dict__,"---------------------")
        if obj.is_valid() :
            
            
            #recaptcha verification bofore save any object in db 
            response = request.POST.get('g-recaptcha-response')
            data = {
                'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response' : response
            }
            data_response = requests.post('https://www.google.com/recaptcha/api/siteverify',data=data)
            result = data_response.json()
            
            if result['success'] :
                obj.save()
            # print("******",obj.__dict__,"---------------------")
                username = obj.cleaned_data.get('username')
                # print(obj.cleaned_data,"---------------------")
                messages.success(request,"welcome {} registration with success ".format(username))
                # print(obj.instance,"*****************")
                # print(obj.instance,"**********************instance instance")
                return redirect('login-path')
            else :
                messages.warning(request,"Invalid recaptcha ! ")
                return redirect('register-path')
        else :
            messages.warning(request," try again ! ")

    return render(request,'blog/register.html',{'form' : UserRegister()})

def login_view(request) :

    if request.method =="POST" :
        x = request.POST.get('username')
        y = request.POST.get('password')
        usr = authenticate(request,username = x, password =y)
        if usr :
            login(request,usr)
            return redirect('home-path')


        else :
            messages.warning (request,'password or username not matching !')

    return render(request,'blog/login.html',{'form' : LoginForm()})


def logout_view(request) :
    auth.logout(request)

    return render(request,'blog/logout.html')


@login_required(login_url = 'login-path')
def profile(request) :
      
    return render(request,'blog/profile.html' , {'profile' :Profile.objects.get(user = request.user),
                                                 
                                                 })


def edit_profile(request) :
    
    
    if request.method == "POST" :
        obj1 = ProfileForm(request.POST ,request.FILES, instance = Profile.objects.get(user=request.user))
        
        obj2 = ProfileFormUser(request.POST, instance= request.user)
        
      #  print(type(request.POST),type(request.FILES), "***********************************************")
       
        if obj1.is_valid() and obj2.is_valid() :
            obj2.save()
            obj1 = obj1.save(commit=True)
            obj1.user = request.user
            obj1.save()
            
            # print(obj1.__dict__,"*****************")

            return redirect('profile-path')
            
            
    
    return render(request,'blog/edit_profile.html', 
                  {'form_profile':ProfileForm(instance=Profile.objects.get(user =request.user)),
                  'form_user':ProfileFormUser(instance=User.objects.get(username=request.user)),
                   'profile' :Profile.objects.get(user = request.user)
                                                    })

