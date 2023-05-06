from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from app.forms import *
# Create your views here.
def home(request):
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
        


          