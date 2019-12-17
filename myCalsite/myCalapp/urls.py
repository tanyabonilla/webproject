from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',  views.index),
    #path('calendar/', views.index),
    path('logout/', views.logout_view),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('myfriends/', views.add_remove_friend),
    path('myfriends/friends/', views.friends_view), #json
    path('chat/', views.chatindex, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('new_events_tasks/', views.new_events_tasks), #new_event
    #path('month/', views.index), #monthly
    path('events/', views.events_view), #json
    path('new_events_tasks/events/', views.events_view), #json
    path('tasks/', views.tasks_view), #json
    path('new_events_tasks/tasks/', views.tasks_view), #json
    path('friends/', views.friends_view), #json

]