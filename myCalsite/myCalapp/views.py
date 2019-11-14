from django.shortcuts import render
from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt

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
           new_eventu = models.Event_user(eventu_name = form_instance_eu.cleaned_data['feventu_name'],
           eventu_startday = form_instance_eu.cleaned_data['feventu_startday'],
           eventu_starttime = form_instance_eu.cleaned_data['feventu_starttime'],
           eventu_endday = form_instance_eu.cleaned_data['feventu_endday'],
           eventu_endtime = form_instance_eu.cleaned_data['feventu_endtime'],
           eventu_location = form_instance_eu.cleaned_data['feventu_location'],
           eventu_note = form_instance_eu.cleaned_data['feventu_note'],
           eventu_tag = form_instance_eu.cleaned_data['feventu_tag'],
            )
           new_eventu.save() #goes into the database
           form_instance_eu = forms.Eventuser_Form()#clears the form out if its good
           
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

