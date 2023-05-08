from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    
    return render(request,'home.html')
    






def registration(request):
    UFO=UserForm()
    PFO=ProfileForm()                                                      
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
           
            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()

            send_mail('registration',
                    "successfull registration is done",
                    'kreddyprasanna6@gmail.com',
                    [NSUO.email],fail_silently=True
                    )
            
                     
            return HttpResponse('registration is successful')
        else:
            return HttpResponse('not valid')
    
    return render(request,'registration.html',d)
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid username or password')
    return render(request,'user_login.html')

@login_required 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



          