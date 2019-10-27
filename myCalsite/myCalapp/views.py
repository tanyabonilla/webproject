from django.shortcuts import render
from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt

#from . import models
#from . import forms
# Create your views here.

def index(request):

    #n=range(1,10*page+10) #shows 10 num per page
    #"reasons_list": n[page*9: (page*9+9)],
    #n=range(1,10*page+10) #show 9 pages

    #n = models.Post.objects.all()
    #e = models.Event.objects.all()

    cins = "CINS465"
    context = {
        "title":"Home",
        "welcome":"Hello World",
        #"reasons_list": n[0:9],
        #"index_list": n[0:9],
        #"event_list":e[0:9],
        "course": cins,  
        "opening":"Hi, welcome to fall semester CINS465",
        # "form": form_instance,
        # "eventform": event_instance,
    }
    #if page is home return home.html
    return render(request, "index.html", context=context)
    #return HttpResponse("CINS465 Hello World")
