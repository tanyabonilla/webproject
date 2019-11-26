from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import forms
# Create your views here.

def index(request):
    
    #n=range(1,10*page+10) #shows 10 num per page
    #"reasons_list": n[page*9: (page*9+9)],
    #n=range(1,10*page+10) #show 9 pages

    if request.method == "POST":
        print("POST")
        form_instance_eu = forms.Eventuser_Form(request.POST)
        if form_instance_eu.is_valid():
            form_instance_eu.save_eventu(request=request)
            form_instance_eu = forms.Eventuser_Form()#clears the form out if its good
            return HttpResponseRedirect("/Calendar/") #redirect to new page
        else:
            return HttpResponseRedirect("/Calendar/") #redirect somewhere else
    else:
        form_instance_eu = forms.Eventuser_Form()
        
    #print(request.method)

    e = models.Event_user.objects.all()

    cins = "CINS465"
    context = {
        "title":"Home",
        "welcome":"Hello World",
        #"reasons_list": n[0:9],
        #"index_list": n[0:9],
        "eventu_list":e[0:9],
        "course": cins,  
        "opening":"Hi, welcome to fall semester CINS465",
        "form_eventu": form_instance_eu,
        #"eventuform": eventu_instance,
    }
    #if page is home return home.html
    return render(request, "index.html", context=context)

def show_Calendar(request, page=0):
    myDate = datetime.now()

    context = {
        'date': formatedDate
    }
    return render(request, "index.html", context=context)

def register(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return HttpResponseRedirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login/")