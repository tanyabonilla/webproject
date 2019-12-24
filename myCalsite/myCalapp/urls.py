from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('logout/', views.logout_view),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('myfriends/', views.add_remove_friend),
    path('myfriends/friends/', views.friends_view),  #json
    path('friends/', views.friends_view), #json
    path('chat/', views.chatindex, name='chat'),
    path('chat/chatrooms/', views.chatrooms_view), #json
    path('chat/<str:room_name>/', views.room, name='room'),
    path('chat/events/', views.room, name='room'),
    path('chat/tasks/', views.room, name='room'),
    path('chat/friends/', views.room, name='room'),
    path('events/', views.events_view),  #json
    path('tasks/', views.tasks_view),  #json
    path('chatrooms/', views.chatrooms_view), #json
    path('new_events_tasks/', views.new_events_tasks), #new_event
    path('new_events_tasks/events/', views.events_view), #json
    path('new_events_tasks/tasks/', views.tasks_view),  #json
    path('new_events_tasks/friends/', views.friends_view),  #json
    path('new_events_tasks/chatrooms/', views.chatrooms_view), #json
    path('mytasks/', views.mytask_view),
    path('mytasks/tasks/', views.tasks_view),  #json
    path('mytasks/events/', views.events_view),  #json
    path('mytasks/friends/', views.friends_view), #json
    path('mytasks/chatrooms/', views.chatrooms_view), #json
]