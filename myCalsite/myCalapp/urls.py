from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',  views.index),
    path('Calendar/', views.index),
   
    #path('<int:page>/', views.index),
    # path('month/<int:page>/', views.index), <--will be doing something like this
    path('logout/', views.logout_view),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('myfriends/', views.add_remove_friend),
    path('chat/', views.chatindex, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    #path('events/', views.events_view),
]
