from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index), #landing page
    path('register/', views.register), #register
    path('login/', auth_views.LoginView.as_view()), #login
    path('logout/', views.logout_view), #logout
    path('calendar/', views.index), #calendar
    path('calendar/month/', views.index) #monthly
    #path('<int:page>/', views.index),
    #path('month/<int:page>/', views.index), <--will be doing something like this
    
#FUTURE VIEWS
    #path('calendar/week', views.index), #weekly
    #path('calendar/daily', views.index) #daily
    #path('tasks/', views.profile), #tasks
    #path('profile/', views.profile), #profile
]
