from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view()),
    #path('<int:page>/', views.index),
    #path('month/<int:page>/', views.index), <--will be doing something like this
    path('login/', auth_views.LoginView.as_view()),
    path('calendar/', views.index),
    path('logout/', views.logout_view),
    path('register/', views.register),
    #path('profile/', views.profile),
    #path('events/', views.events_view),
]
