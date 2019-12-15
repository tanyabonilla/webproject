from django.shortcuts import render, redirect #get_object_or_404 (friends)
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#friends
from django.views.generic.base import RedirectView
from django.db import transaction
from django.shortcuts import get_object_or_404
#for chat
from django.utils.safestring import mark_safe
import json

from . import models
from . import forms
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    
#     #n=range(1,10*page+10) #shows 10 num per page
#     #"reasons_list": n[page*9: (page*9+9)],
#     #n=range(1,10*page+10) #show 9 pages

    if request.method == "POST":
        print("POST index")
        if request.user.is_authenticated:
            if 'submit_tasku' in request.POST:
                form_instance_tu = forms.Taskuser_Form(request.POST)
                if form_instance_tu.is_valid():
                    form_instance_tu.save_tasku(request=request)
                    form_instance_tu = forms.Taskuser_Form()#clears the form out if its good
                    return redirect("/") 
                else:
                    return redirect("/") #redirect somewhere else
            if 'submit_eventu' in request.POST:
                form_instance_eu = forms.Eventuser_Form(request.POST)
                if form_instance_eu.is_valid():
                    form_instance_eu.save_eventu(request=request)
                    form_instance_eu = forms.Eventuser_Form()#clears the form out if its good
                    return redirect("/") 
                else:
                    return redirect("/") #redirect somewhere else
        else:
            form_instance_eu = forms.Eventuser_Form()
            form_instance_tu = forms.Taskuser_Form()
    else:
        form_instance_eu = forms.Eventuser_Form()
        form_instance_tu = forms.Taskuser_Form()

    #gets/shows the current users tasks and events
    try:
        all_events = models.Event_user.objects.filter(user_ID=request.user.id)
    except models.Event_user.DoesNotExist:
        all_events = None

    try:
        all_tasks = models.Task_user.objects.filter(user_ID=request.user.id)
    except models.Task_user.DoesNotExist:
        all_tasks = None

    friend_object = models.Friendship.objects.get(user=request.user)
    all_friends = [friend for friend in friend_object.friends.all() if friend != request.user]

    cins = "CINS465"
    context = {
        "title":"Home",
        "welcome":"Hello",
        "current_user":request.user,
        #"reasons_list": n[0:9],
        #"index_list": n[0:9],
        "tasku_list":all_tasks,
        "eventu_list":all_events,
        "friend_list":all_friends,
        "course": cins,  
        "opening":"Hi, welcome to fall semester CINS465",
        "form_tasku": form_instance_tu,
        "form_eventu": form_instance_eu,
        #"eventuform": eventu_instance,
    }
#     #if page is home return home.html
    return render(request, "index.html", context=context)

@login_required(login_url='/login/')
def tasks_view(request):
    if request.method == 'GET':
        try:
            task_query = models.Task_user.objects.filter(user_ID=request.user.id).order_by('-tasku_duedate')
            currtask_list = {"tasks":[]}
            for t_q in task_query:
                currtask_list["tasks"] += [{
                    "user": t_q.user_ID.username,
                    "t_name": t_q.tasku_name,
                    "t_duedate": t_q.tasku_duedate,
                    "t_note": t_q.tasku_note,
                    "t_tag": t_q.tasku_tag,
                    }]
        except models.Task_user.DoesNotExist:
            currtask_list = None
        return JsonResponse(currtask_list) 
    else: HttpResponse("Unsupported HTTP Method")

@login_required(login_url='/login/')
def events_view(request):
    if request.method == 'GET':
        try:
            event_query = models.Event_user.objects.filter(user_ID=request.user.id).order_by('-eventu_startday')
            currevent_list = {"events":[]}
            for e_q in event_query:
                currevent_list["events"] += [{
                    "user": e_q.user_ID.username,
                    "e_name": e_q.eventu_name,
                    "e_startdate": e_q.eventu_startday,
                    "e_starttime": e_q.eventu_starttime,
                    "e_enddate": e_q.eventu_endday,
                    "e_endtime": e_q.eventu_endtime,
                    "e_location": e_q.eventu_location,
                    "e_note": e_q.eventu_note,
                    "e_tag": e_q.eventu_tag
                    }]
        except models.Task_user.DoesNotExist:
            currevent_list = None
        return JsonResponse(currevent_list) 
    else: HttpResponse("Unsupported HTTP Method")

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
            user = form_instance.save()
            # form_instance.save_profile(user)
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    context = {
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=context)

def logout_view(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url='/login/')
def add_remove_friend(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if 'submit_afriend' in request.POST:
                print("POST add_friend")
                form_instance_addFriend = forms.Add_FriendForm(request.POST)
                if form_instance_addFriend.is_valid():
                    print("Valid")
                    form_instance_addFriend.save_friend(request=request)
                    form_instance_addFriend = forms.Add_FriendForm()#clears the form out if its good
                    return redirect("/myfriends/") #redirect to new page
                else:
                    print("Not Valid")
                    return redirect("/myfriends/") #redirect to new pagee
            if 'submit_enemy' in request.POST:
                form_instance_removeFriend = forms.Remove_FriendForm(request.POST)
                if form_instance_removeFriend.is_valid():
                    print("Valid")
                    form_instance_removeFriend.save_rfriend(request=request)
                    form_instance_removeFriend = forms.Remove_FriendForm()#clears the form out if its good
                    return redirect("/myfriends/") #redirect to new page
                else:
                    print("Not Valid")
                    return redirect("/myfriends/") #redirect to new pagee
        else:
            form_instance_addFriend = forms.Add_FriendForm()
            form_instance_removeFriend = forms.Remove_FriendForm()
    else:
        form_instance_addFriend = forms.Add_FriendForm()
        form_instance_removeFriend = forms.Remove_FriendForm()

    friend_object = models.Friendship.objects.get(user=request.user)
    all_friends = [friend for friend in friend_object.friends.all() if friend != request.user]

    #n=range(1,10*page+10) #shows 10 num per page
     #"reasons_list": n[page*9: (page*9+9)],

    context = {
        "current_user":request.user,
        "add_form":form_instance_addFriend,
        "remove_form":form_instance_removeFriend,
        "friend_list":all_friends,
    }
    return render(request, "friends.html", context=context)

@login_required(login_url='/login/')
def chatindex(request):
    context = {
        "current_user":request.user,
    }
    return render(request, 'chat/chatindex.html', context=context)

@login_required(login_url='/login/')
def room(request, room_name):
    context = {
        "current_user":request.user,
        'room_name_json': mark_safe(json.dumps(room_name)),
    }
    return render(request, 'chat/room.html',  context=context)